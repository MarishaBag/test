from sqlalchemy import create_engine, Table, Column, Integer, Date, String, DateTime, MetaData, ForeignKey

meta = MetaData()

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('user_name', String(255), nullable=False),
    Column('password', String(8),nullable=False),
    Column('created_at', Date, nullable=False),
    Column('updated_at', Date)
)

booking = Table(
    'booking', meta,
    Column('id', Integer, nullable=False),
    Column('user_id', ForeignKey(user.c.id)),
    Column('start_time', DateTime, nullable=False),
    Column('end_time', DateTime, nullable=False),
    Column('comment', String(255))
)

engine = create_engine("mysql+mysqlconnector://root:password@localhost/test", echo=True)
meta.create_all(engine)
conn = engine.connect()
