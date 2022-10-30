from re import compile as re_compile
from requests import get, exceptions, Timeout
#raetarvq_bot
#t.me/raetarvq_bot
#5708021739:AAEuFlb0tK6UjUKebyp5-1dch2WG021ABIQ
#https://api.telegram.org/bot5708021739:AAEuFlb0tK6UjUKebyp5-1dch2WG021ABIQ/getMe
#get the chat_id : #https://api.telegram.org/bot5708021739:AAEuFlb0tK6UjUKebyp5-1dch2WG021ABIQ/getUpdates

class Telegram():
    """Telegram client"""

    def __init__(self, token='', client_id=''):
        """Create telegram class defaults"""
        self.api = 'https://api.telegram.org/bot'
        self._token = token
        self._client_id = str(client_id)

        p = re_compile(r"^\d{1,10}:[A-z0-9-_]{35,35}$")
        if not p.match(token):
            raise Exception('Telegram token is invalid')

        p = re_compile(r"^-?\d{7,13}$")
        if not p.match(client_id):
            raise Exception('Telegram client_id is invalid')
        print('Telegram configure with for client "' + client_id + '" with token "' + token + '"')

    def send(self, message='', parsemode='Markdown') -> str:
        """Send telegram message"""

        try:
            escaped_message = message.translate(message.maketrans({"*":  r"\*"}))
            payload = f'{self.api}{self._token}/sendMessage?chat_id={self._client_id}&parse_mode={parsemode}&text={escaped_message}'
            resp = get(payload)
            print(f'staus code is {resp.status_code}')
            if resp.status_code != 200:
                return ''

            resp.raise_for_status()
            json = resp.json()

        except exceptions.ConnectionError as err:
            print(err)
            return ''

        except exceptions.HTTPError as err:
            print(err)
            return ''

        except Timeout as err:
            print(err)
            return ''

        return json

if __name__=='__main__':

    telegram = Telegram(token='5708021739:AAEuFlb0tK6UjUKebyp5-1dch2WG021ABIQ', client_id='5568877721')
    message = "I am a robot"
    telegram.send(message)
    #message = 'un message'
    #print(message.translate(message.maketrans({"*":  r"\*"})))
    #message.translate()
