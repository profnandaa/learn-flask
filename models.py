
import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
 
Base = declarative_base()

engine = create_engine('sqlite:///db/app.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	password = Column(String(100))

	def save(self):
		session.add(self)
		session.commit()

class Blog(Base):
	__tablename__ = 'blog'
	id = Column(Integer, primary_key=True)
	name = Column(Strinzg(250), nullable=False)
	url = Column(String(100), unique=True)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

class Post(Base):
	__tablename__ = 'post'
	id = Column(Integer, primary_key=True)
	title = Column(String(250), nullable=False)
	body = Column(Text)
	date_time = Column(DateTime, default=datetime.datetime.utcnow)
	blog_id = Column(Integer, ForeignKey('blog.id'))
	blog = relationship(Blog)


# to run migrations (sort of)
if __name__ == '__main__':
	Base.metadata.create_all(engine)


