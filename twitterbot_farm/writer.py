from bot import Bot
from dictator import Dictator


class Writer(Bot):

    """ Reads tweets from reader db. Templating, filter (rate and duplicate) and post. """

    def __init__(self, username,):
        Bot.__init__(self, username)
        self.last_tweet_id = int(self.connection.get('__last_tweet_id__', 1))
        self.reader = Dictator(self.reader_db_id)
        self.analyzer = Dictator(self.analyzer_db_id)

    def tweet(self):
        pass

    def is_already_posted(self, words):
        return self.connection.get(words)

    def is_words_bad(self, words):
        return any(int(self.analyzer.get(word)) < -10 for word in words)
