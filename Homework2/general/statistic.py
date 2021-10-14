from collections import Counter
from utils import format_text
from general.base import BaseAnalyzer


class Statistic(BaseAnalyzer):

    @format_text
    def get_statistic(self):
        return {
            'Number of characters': self._characters_number(),
            'Number of words': self._words_number(),
            'Number of sentences': self._sentences_number(),
            'Frequency of characters': self._characters_frequency(),
            'Distribution of characters as a percentage of total': self._characters_distribution(),
            'Average word length': self._words_average_length(),
            'The average number of words in a sentence': self._words_average_number(),
            'Is the whole text a palindrome?': self._is_text_palindrome(),
        }

    def _characters_number(self):
        return len(self.input_text)

    def _words_number(self):
        return len(self._get_words())

    def _sentences_number(self):
        sentences = self._get_sentences()
        return len(sentences)

    def _characters_frequency(self):
        return ' '.join([f'"{k}": {v} |' for k, v in Counter(self.input_text).items()])

    def _characters_distribution(self):
        c = Counter(self.input_text)
        return ' '.join([f'"{i}": {round(c[i]/(len(self.input_text)) * 100.0, 1)}% |' for i in c])

    def _words_average_length(self):
        words_length = [len(i) for i in self._get_words()]
        return round(sum(words_length)/len(words_length))

    def _words_average_number(self):
        sentences = self._get_sentences()
        sentences_length = [len(s.split()) for s in sentences]
        return round(sum(sentences_length) / len(sentences_length))

    def _is_text_palindrome(self):
        t = ''.join([c for c in self.input_text if c.isalpha])
        return 'Yes' if t == t[::-1] else 'No'
