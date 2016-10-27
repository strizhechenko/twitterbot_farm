from bot import Bot


class Writer(Bot):

    """ Reads tweets from reader db. Templating, filter (rate and duplicate) and post. """

    def __init__(self, username, host='127.0.0.1'):
        Bot.__init__(self, username, host)
        self.last_tweet_id = int(self.connection.get('__last_tweet_id__', 1))

    def tweet(self, key, tweet, result):
        tweet_rc = self.twibot.api.update_status(tweet)
        # pylint: disable=E1101
        self.connection[result] = tweet_rc.id
        self.connection['__last_tweet_id__'] = key

    def unprocessed_lines(self):
        return [(key, value) for key, value in self.reader.items() if key.isdigit() and int(key)
                > int(self.last_tweet_id)]

    def is_already_posted(self, words):
        return self.connection.get(words)

    def is_words_bad(self, words):
        return any(int(self.analyzer.get(word)) < -10 for word in words)
