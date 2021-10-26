from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# TODO: Add your models below this line!

class User(Base):
	__tablename__ = 'users'
	name = Column(String)
	email = Column(String, primary_key=True)
	word = Column(String)
	donate = Column(Integer)