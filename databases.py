from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# TODO: Add your database functions below this line!

def add_user(name, email, word):
    user_object = User(name= name, email= email, word= word)
    session.add(user_object)
    session.commit()

def get_user_by_mail(email):
  user = session.query(User).filter_by(email=email).first()
  return user