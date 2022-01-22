from unittest import TestCase

from Homework2.general.statistic import Statistic
from tests.constants import INPUT_TEXT


class StatisticTest(TestCase):
    def setUp(self) -> None:
        self.inst = Statistic(INPUT_TEXT)

    def test_is_text_palindrome(self):
        result = self.inst._is_text_palindrome()
        self.assertEqual(result, 'No')
