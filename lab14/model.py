from sqlalchemy import Column, Integer, String, ForeignKey, Table, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("Lessons.id")),
    Column("right_id", ForeignKey("Disciplines.id")),
)

association_table2 = Table(
    "association_table2",
    Base.metadata,
    Column("right_id", ForeignKey("Disciplines.id")),
    Column("third_id", ForeignKey("Days of week.id")),
)

class Lessons(Base):
    __tablename__ = 'Lessons'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    start = Column(Time)
    end = Column(Time)
    numbers = relationship('Disciplines', secondary=association_table, back_populates="lessons")

    def __repr__(self):
        return f'<n={self.number}, s={self.start}, date={self.end}>'


class Disciplines(Base):
    __tablename__ = 'Disciplines'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lessons = relationship('Lessons', secondary=association_table,  back_populates='numbers')
    days = relationship('DaysOfWeek', secondary=association_table2, back_populates="disciplines")

    def __repr__(self):
        return self.name


class DaysOfWeek(Base):
    __tablename__ = 'Days of week'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    disciplines = relationship('Disciplines', secondary=association_table2,  back_populates='days')

    def __repr__(self):
        return self.name
