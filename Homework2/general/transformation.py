from general.base import BaseAnalyzer
from utils import format_text


class Transformation(BaseAnalyzer):

    @format_text
    def transform(self):
        return{
            'The reversed text': self._reverse_text(),
        }

    def _reverse_text(self):
        return self.input_text[::-1]
