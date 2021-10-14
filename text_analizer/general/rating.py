from collections import Counter
from utils import format_text
from general.base import BaseAnalyzer


class Rating(BaseAnalyzer):

    @format_text
    def rate_text(self):
        return {
            'Top 10 most used words': self._most_used_words(),
            'Top 10 longest words': self._longest_words(),
            'Top 10 shortest words': self._shortest_words(),
            'Top 10 longest sentences': self._longest_sentences(),
            'Top 10 shortest sentences': self._shortest_sentences(),
            'Top 10 longest palindrome words': self._longest_palindrome_words(),
        }

    def _most_used_words(self, count=10):
        return ', '.join([i[0] for i in Counter(self._get_words()).most_common(count)])

    def _longest_words(self, count=10):
        return ', '.join(sorted(self._get_words(), reverse=True, key=lambda i: len(i))[:count])

    def _shortest_words(self, count=10):
        return ', '.join(sorted(self._get_words(), key=lambda i: len(i))[:count])

    def _longest_sentences(self, count=10):
        return ', '.join(sorted(self._get_sentences(), reverse=True, key=lambda i: len(i))[:count])

    def _shortest_sentences(self, count=10):
        return ', '.join(sorted(self._get_sentences(), key=lambda i: len(i))[:count])

    def _longest_palindrome_words(self, count=10):
        return sorted(self._get_palindromes(), reverse=True, key=lambda i: len(i))[:count]
