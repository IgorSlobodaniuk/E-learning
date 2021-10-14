from nltk.tokenize import sent_tokenize


class BaseAnalyzer:
    def __init__(self, input_text):
        self.input_text = input_text

    def _get_characters(self):
        return self.input_text

    def _get_words(self):
        return self.input_text.split()

    def _get_sentences(self):
        return sent_tokenize(self.input_text)

    def _get_palindromes(self):
        return [w for w in self._get_words() if w == w[::-1]]


