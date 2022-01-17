from sqlalchemy import Table, Column, Integer, String, MetaData, Text, ForeignKey
meta = MetaData()


text_edition = Table(
   'text_edition', meta,
   Column('id', Integer, primary_key=True),
   Column('origin', Text),
   Column('statistic', Text),
   Column('rating', Text),
   Column('transformation', Text),

)
