from inspect import getsourcefile
import os
import json


class GerSent:
    def __init__(self, algorithm: str = "simple"):
        self._algorithm = algorithm

        self._check()
        self._load_algorithm()

    def sentiment(self, sentence: str):
        return self.sentiment_instance.sentiment(sentence)

    def _check(self):
        pass

    def _load_algorithm(self):
        if self._algorithm is "simple":
            self.sentiment_instance = SimpleSentiment()


class SimpleSentiment:
    WORDLIST_POSITIVE_PATH = "wordlists/de/positive.json"
    WORDLIST_NEGATIVE_PATH = "wordlists/de/negative.json"

    def __init__(self):
        _this_module_file_path_ = os.path.abspath(getsourcefile(lambda: 0))
        self.WORDLIST_POSITIVE_PATH = os.path.join(
            os.path.dirname(
                _this_module_file_path_), self.WORDLIST_POSITIVE_PATH
        )
        self.WORDLIST_NEGATIVE_PATH = os.path.join(
            os.path.dirname(
                _this_module_file_path_), self.WORDLIST_NEGATIVE_PATH
        )

        self.wordlist_negative = {}
        self.wordlist_positiv = {}

        self._load()

    def _load(self):
        self.wordlist_negative = self._load_json(self.WORDLIST_NEGATIVE_PATH)
        self.wordlist_positiv = self._load_json(self.WORDLIST_POSITIVE_PATH)

    def _load_json(self, path: str):
        with open(path, "r") as fp:
            return json.load(fp)

    def sentiment(self, sentence: str):
        return self._algorithm(sentence)

    def _algorithm(self, sentence: str):
        sentence_preprocessed = self._preprocessing(sentence)
        negative_score = self._evaluate(
            sentence_preprocessed, self.wordlist_negative)
        positive_score = self._evaluate(
            sentence_preprocessed, self.wordlist_positiv)

        multiplier = self.multiplier(sentence)
        negative_score *= multiplier
        positive_score *= multiplier

        return {
            "negative": negative_score,
            "positive": positive_score,
            "composite": negative_score + positive_score,
        }

    def _evaluate(self, sentence, wordlist):
        words = sentence.split(" ")
        score = 0.0
        for word in words:
            if word in wordlist:
                score += float(wordlist[word])
        return score

    def _preprocessing(self, sentence: str):
        return sentence.replace(".", "").replace("!", "").replace(",", "")

    # TODO (Bernhard): "Ich bin ein guter Satz! "
    # TODO (Bernhard): "Ich bin ein guter Satz!!!!"
    def multiplier(self, sentence: str):
        multiplier = 1.0
        multiplier += self.last_symbol(sentence)
        return multiplier

    def last_symbol(self, sentence):
        if sentence[-1] is '!':
            return 0.1
        return 0.0
