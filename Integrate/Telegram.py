import requests


class Telegram(object):
    def __init__(self, import_name):
        self.import_name = import_name
        self.update_rules = list()
        self.config = dict(
            api_key=None,
            requests_kwargs=dict(
                timeout=60,
            ),
        )
        self.offset = 0
        self.whoami = None

    def _bot_cmd(self, method, endpoint, *args, **kwargs):
        base_api = "https://api.telegram.org/bot{api_key}/{endpoint}"
        endpoint = base_api.format(api_key=self.config['api_key'], endpoint=endpoint)

        try:
            response = method(endpoint, data=kwargs.get('data', None), params=kwargs.get('params', {}),
                              **self.config['requests_kwargs'])

            if response.status_code != 200:
                raise ValueError('Got unexpected response. ({}) - {}'.
                                 format(response.status_code, response.text))

            return response.json()
        except Exception as e:
            return {
                'ok': False,
                'error': str(e),
            }

    def get_updates(self, timeout=0, offset=None):
        params = dict(
            timeout=timeout,
            offset=offset,
        )
        return self._bot_cmd(requests.get, 'getUpdates', params=params)

    def get_me(self):
        return self._bot_cmd(requests.get, 'getMe')

    def send_message(self, chat_id, text):
        data = dict(
            chat_id=chat_id,
            text=text,
        )

        return self._bot_cmd(requests.post, 'sendMessage', data=data)
