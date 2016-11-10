from re import sub
from bot import Bot


class Analyzer(Bot):
    """
    1. Reads writer feed
    2. counts likes/retweets
    3. modifies words/phrases rates
    """

    def __init__(self, username, host='127.0.0.1'):
        Bot.__init__(self, username, host)
        self.last_tweet_id = int(self.connection.get('__last_tweet_id__', 1))

    def fetch(self, logging=True):
        """ fetch as many own tweets as we can """
        if logging:
            print "fetch..."
        source = self.twibot.api.me().timeline
        tweets = []
        tweets_temp = source(count=200)
        while tweets_temp:
            tweets.extend(tweets_temp)
            if logging:
                print "200 more... now:", len(tweets)
            tweets_temp = source(count=200, max_id=tweets_temp[-1].id - 1)
        return tweets

    def update_rates(self, word_count=2):
        """ update rates of all latest availble tweets (likes + rt * 3) """
        template_phrase = sub('{.*', '', self.template)
        for tweet in self.fetch():
            words = tweet.text.encode('utf-8').replace(template_phrase, '')
            if len(words.split()) != word_count:
                continue
            likes = tweet.favorite_count + tweet.retweet_count * 3
            self.analyzer[words] = likes
            print tweet.id, words, likes

    def best(self):
        """ return: dict of tweets with rate more than 0 """
        return {key: rate for key, rate in self.analyzer.items() if int(rate) > 0}

    def print_best(self):
        """ print best tweets in descending rate order """
        for words, rate in sorted(self.best().items(), key=lambda x: int(x[1]), reverse=True):
            print self.template.format(words), "\t\t\t\t", rate

    def cleanup(self):
        """ remove all tweets those had not been liked """
        for tweet in self.fetch():
            if tweet.favorite_count == tweet.retweet_count == 0:
                tweet.destroy()
