
# Basic models for demostration
import os
import sys
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

 
Base = declarative_base()

engine = create_engine('sqlite:///db/sample.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class Post(Base):
	__tablename__ = 'post'
	id = Column(Integer, primary_key=True)
	title = Column(String(250), nullable=False)
	body = Column(Text)
	date_time = Column(DateTime, default=datetime.datetime.utcnow)

	def save(self):
		session.add(self)
		session.commit()


# to run migrations (sort of)
if __name__ == '__main__':
	Base.metadata.create_all(engine)


