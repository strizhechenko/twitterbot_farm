from dictator import Dictator
from twitterbot_utils import Twibot


# pylint: disable=R0903
class Bot(object):
    """ redis/auth manager and Twibot connector """

    def __init__(self, username, host='127.0.0.1'):
        auth = Dictator(host=host)
        consumer_key, consumer_secret = auth.get('__app__')
        _, db_id, access_token, access_secret = auth.get('@' + username)
        self.connection = Dictator(host=host, db=db_id)
        self.twibot = Twibot(method='params',
                             consumer_key=consumer_key,
                             consumer_secret=consumer_secret,
                             access_token=access_token,
                             access_secret=access_secret)
