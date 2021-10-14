from datetime import datetime
from general.statistic import Statistic
from general.rating import Rating
from general.transformation import Transformation
from time import perf_counter


def analyze(text):
    start = perf_counter()
    s = Statistic(text)
    r = Rating(text)
    t = Transformation(text)
    print(s.get_statistic(), '\n')
    print(r.rate_text(), '\n')
    print(t.transform(), '\n')
    print(f'Date and time when the report was generated: {datetime.now()}')
    end = perf_counter()
    print('Duration: ', round(end - start, 2))


if __name__ == '__main__':
    analyze(text=input('Enter the text: '))
