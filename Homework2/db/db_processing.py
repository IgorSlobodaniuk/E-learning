from sqlalchemy import insert
from db.connection import engine
from db.orm import text_edition


def add_new_record(text, rating, statistic, transformation):
    conn = engine.connect()
    ins = text_edition.insert().values(
        origin=text,
        statistic=statistic,
        rating=rating,
        transformation=transformation,
    )

    conn.execute(ins)
    conn.close()
