
# Basic models for demonstration

import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship, sessionmaker

 
Base = declarative_base()

engine = create_engine('sqlite:///db/app.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	first_name = Column(String(100))
	last_name = Column(String(100))
	username = Column(String(100), nullable=False)
	email = Column(String(100))
	password = Column(String(100))

	def save(self):
		session.add(self)
		session.commit()

class Post(Base):
	__tablename__ = 'post'
	id = Column(Integer, primary_key=True)
	title = Column(String(250), nullable=False)
	body = Column(Text)
	date_time = Column(DateTime, default=datetime.datetime.utcnow)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	def save(self):
		session.add(self)
		session.commit()

