from datetime import datetime
from general.statistic import Statistic
from general.rating import Rating
from general.transformation import Transformation
from time import perf_counter
from db.db_processing import add_new_record


def analyze(text):
    start = perf_counter()
    s = Statistic(text)
    r = Rating(text)
    t = Transformation(text)
    statistic = s.get_statistic()
    rating = r.rate_text()
    transformation = t.transform()
    print(f'Date and time when the report was generated: {datetime.now()}')

    add_new_record(
        text=text,
        statistic=statistic,
        rating=rating,
        transformation=transformation
    )
    end = perf_counter()
    print('Duration: ', round(end - start, 2))


if __name__ == '__main__':
    analyze(text=input('Enter the text: '))
