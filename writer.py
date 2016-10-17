from bot import Bot
from dictator import Dictator


class Writer(Bot):

    def __init__(self, username, host, db):
        Bot.__init__(username, host, db)
        self.last_tweet_id = int(self.connection.get('__last_tweet_id__', 0))
        self.rates = Dictator(username + '_rate', host, db)

    def tweet(self):
        pass

    def is_already_posted(self, words):
        return self.connection.get(words)

    def is_words_bad(self, words):
        return any(int(self.rates.get(word)) < 10 for word in words)
