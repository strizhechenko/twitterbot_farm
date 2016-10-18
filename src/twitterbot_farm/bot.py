from dictator import Dictator
from twitterbot_utils import Twibot


class Bot(object):

    def __init__(self, host, db, username):
        self.connection = Dictator(host=host, db=db)
        self.twibot = Twibot(username)
