# CRUD = Create, Read, Update, Delete
from config import DATABASE_URI
from model import Lessons, Disciplines, DaysOfWeek, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from random import choice, randint
from datetime import date


def get_session_engine(db_uri):
    engine = create_engine(db_uri)#, echo=True)
    session = scoped_session(sessionmaker(bind=engine))
    return session, engine


def create_database(db_uri):
    session, engine = get_session_engine(db_uri)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return session


def fill_db(session):

    def read_csv(name):
        with open(f'./static_data/{name}.csv', 'r', encoding='utf_8_sig') as f:
            result = [line.strip() for line in f]
        return result

    lessons = [(l.split(';')[0], l.split(';')[1], l.split(';')[2]) for l in read_csv('lessons')]
    disciplines = read_csv('disciplines')
    days_of_week = read_csv('days_of_week')

    for l in lessons:
        les = Lessons(number=int(l[0]), start=l[1], end=l[2])
        session.add(les)

    for d in disciplines:
        dis = Disciplines(name=d)
        session.add(dis)

    for w in days_of_week:
        dow = DaysOfWeek(name=w)
        session.add(dow)

    for i in range(29):
        p = Lessons()
        c = Disciplines()
        p.numbers.append(c)
        session.add(p)
        #disc = Disciplines(name=randint(1, len(disciplines)))
        #days = DaysOfWeek(name=randint(1, len(days_of_week)))
        #session.add(disc)
        #session.add(days)
        d = DaysOfWeek()
        c.days.append(d)
        session.add(c)
    session.commit()


if __name__ == '__main__':
    print('connecting...')

    session = create_database(DATABASE_URI)

    fill_db(session)
    print('db created!')

    session.close()
    print('session closed')