""" redis/auth manager and Twibot connector """

from dictator import Dictator
from twitterbot_utils import Twibot


# pylint: disable=R0903
class Bot(object):
    """ redis/auth manager and Twibot connector """

    def __init__(self, username, host='127.0.0.1'):
        auth = Dictator(host=host)
        consumer_key, consumer_secret = auth.get('__app__')
        user = auth.get('@' + username)
        role, db_id, access_token, access_secret = user[:4]
        if role == 'writer':
            reader_id, analyzer_id, self.template = user[4:7]
            self.reader = Dictator(host=host, db=reader_id)
            self.analyzer = Dictator(host=host, db=analyzer_id)
        self.connection = Dictator(host=host, db=db_id)
        self.twibot = Twibot(method='params',
                             consumer_key=consumer_key,
                             consumer_secret=consumer_secret,
                             access_token=access_token,
                             access_secret=access_secret)
