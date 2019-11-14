from SimpleSentiment import SimpleSentiment


class Gersenti():
    def __init__(self, algorithm: str = 'simple'):
        self._algorithm = algorithm

        self._check()
        self._load_algorithm()

    def sentiment(self, sentence: str):
        return self.sentiment_instance.sentiment(sentence)

    def _check(self):
        pass

    def _load_algorithm(self):
        if self._algorithm is 'simple':
            self.sentiment_instance = SimpleSentiment()
