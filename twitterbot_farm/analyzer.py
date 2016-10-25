from bot import Bot


class Analyzer(Bot):
    """
    1. Reads writer feed
    2. counts likes/retweets
    3. modifies words/phrases rates
    """

    def __init__(self):
        Bot.__init__(self)
        self.last_tweet_id = int(self.connection.get('__last_tweet_id__', 0))

    def fetch(self):
        pass

    def update_rate(self, word):
        pass
