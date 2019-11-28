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

    PREPROCESSING_REPLACEMENTS = [".", ",", "!", '"', "$", "_"]

    def __init__(self):
        self.wordlist_negative = {}
        self.wordlist_positiv = {}

        self._generate_pathes()
        self._load()

    def _generate_pathes(self):
        """ Generats pathes for the wordlists """
        _this_module_file_path_ = os.path.abspath(getsourcefile(lambda: 0))
        self.WORDLIST_POSITIVE_PATH = os.path.join(
            os.path.dirname(_this_module_file_path_), self.WORDLIST_POSITIVE_PATH
        )
        self.WORDLIST_NEGATIVE_PATH = os.path.join(
            os.path.dirname(_this_module_file_path_), self.WORDLIST_NEGATIVE_PATH
        )

    def _load(self):
        """ Loads wordlists """
        self.wordlist_negative = self._load_json(self.WORDLIST_NEGATIVE_PATH)
        self.wordlist_positiv = self._load_json(self.WORDLIST_POSITIVE_PATH)

    def _load_json(self, path: str):
        """ Loads a json file 
        
        Args:
            path: Path to the file
        
        Return:
            wordlist: A json wordlist | dict
        """

        with open(path, "r") as fp:
            return json.load(fp)

    def sentiment(self, sentence: str):
        """ Calls the algorithm
        
        Args:
            sentence: The sentence which will be calculated

        Return:
            sentiment: The results of the sentence | float
        """
        return self._algorithm(sentence)

    def _algorithm(self, sentence: str):
        """ Performs the algorithm
        
        Args:
            sentence: The sentence which will be calculated

        Return:
            sentiment: The results of the sentence | float
        """
        sentence_preprocessed = self._preprocessing(sentence)
        negative_score = self._evaluate(sentence_preprocessed, self.wordlist_negative)
        positive_score = self._evaluate(sentence_preprocessed, self.wordlist_positiv)

        multiplier = self.multiplier(sentence)

        negative_score *= multiplier
        positive_score *= multiplier

        negation = self._negation(sentence)

        return {
            "negative": negative_score * negation,
            "positive": positive_score * negation,
            "composite": (negative_score + positive_score) * negation,
        }

    def _evaluate(self, sentence: str, wordlist: dict):
        """ Performs the wordlist 
        
        Args:
            sentence: The sentence which will be calculated
            wordlist: Dictionary of a wordlist

        Return:
            sentiment: The results of the sentence | float
        """
        words = sentence.split(" ")
        score = 0.0
        for word in words:
            if word in wordlist:
                score += float(wordlist[word])
        return score

    def _preprocessing(self, sentence: str):
        """ Preprocess the sentence 
        
        Args:
            sentence: The sentence which will be calculated
        
        Return:
            sentence_preprocessed: The preprocessed sentence | str
        """
        for char_ in self.PREPROCESSING_REPLACEMENTS:
            sentence = sentence.replace(char_, "")
        return sentence

    def multiplier(self, sentence: str):
        """ Computes a bunch of multiplier
        
        Args:
            sentence: The sentence which will be calculated
        
        Return:
            multiplier: Calculated multiplier of the sentence | float
        """
        multiplier = 1.0
        multiplier += self.last_symbol(sentence)
        return multiplier

    def last_symbol(self, sentence):
        """ Count "!" for the multiplier
        
        Args:
            sentence: The sentence which will be calculated
        
        Return:
            multiplier for "!"
        """
        return sentence.count("!") * 0.05

    # TODO (Bernhard): Maybe relate nicht to the next value
    def _negation(self, sentence):
        """ Inverse the meaning of the sentence
        
        Args:
            sentence: The sentence which will be calculated
        
        Return:
            inverse: Negation of the meaning | integer (0|1)
        """
        words = sentence.split(" ")
        for word in words:
            if word == "nicht":
                return -1
        return 1

