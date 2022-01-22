from unittest import TestCase, mock

from Homework2.general.rating import Rating
from tests.constants import INPUT_TEXT


class RatingTest(TestCase):
    def setUp(self) -> None:
        self.inst = Rating(INPUT_TEXT)

    @mock.patch('general.base.BaseAnalyzer._get_words')
    def test_most_used_words(self, get_words_mock):
        get_words_mock.return_value = INPUT_TEXT.split()
        expected = 'text, for, testing., My, input, just, Another, And, one, more'
        result = self.inst._most_used_words()
        get_words_mock.assert_called_once()
        self.assertEqual(result, expected)

    @mock.patch('general.base.BaseAnalyzer._get_words')
    def test_longest_words(self, get_words_mock):
        get_words_mock.return_value = INPUT_TEXT.split()
        expected = 'testing., testing., Another, input, text, just, text, more, text, for'
        result = self.inst._longest_words()
        get_words_mock.assert_called_once()
        self.assertEqual(result, expected)

    @mock.patch('general.base.BaseAnalyzer._get_words')
    def test_shortest_words(self, get_words_mock):
        get_words_mock.return_value = INPUT_TEXT.split()
        expected = 'My, for, for, And, one, text, just, text, more, text'
        result = self.inst._shortest_words()
        get_words_mock.assert_called_once()
        self.assertEqual(result, expected)
