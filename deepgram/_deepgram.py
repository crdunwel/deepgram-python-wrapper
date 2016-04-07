import json
from urllib import request


class Deepgram:

    baseURI = 'http://api.deepgram.com/'
    headers = {'Content-Type': 'application/json'}

    def __init__(self, opts=None):
        self.opts = opts if type(opts) is dict else {}

    def _post(self, payload):
        try:
            req = request.Request(self.baseURI,
                                  data=self._authenticatedPayload(payload),
                                  headers=self.headers)
            return request.urlopen(req).read()
        except:
            # TODO exception handling
            pass

    def _resolve(self, data):
        try:
            return json.loads(data.decode('utf-8'))
        except:
            # TODO exception handling
            pass

    def _authenticatedPayload(self, payload):
        payload['userID'] = self.opts['userID']
        return json.dumps(payload).encode('utf-8')

    def getBalance(self):
        return self._resolve(self._post({'action': 'get_balance'}))

    def indexContent(self, data_url):
        return self._resolve(self._post({'action': 'index_content', 'data_url': data_url}))

    def getObjectStatus(self, contentID):
        return self._resolve(self._post({'action': 'get_object_status', 'contentID': contentID}))

    def getObjectTranscript(self, contentID):
        return self._resolve(self._post({'action': 'get_object_transcript', 'contentID': contentID}))

    def objectSearch(self, query):
        payload = query if type(query) is dict else {}
        payload['action'] = 'object_search'
        return self._resolve(self._post(payload))

    def groupSearch(self, query):
        payload = query if type(query) is dict else {}
        payload['action'] = 'group_search'
        return self._resolve(self._post(payload))
