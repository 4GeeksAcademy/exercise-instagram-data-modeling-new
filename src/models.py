import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    User_ID = Column(Integer, ForeignKey('follower.User_from_ID'))
    Username = Column(String(20), ForeignKey('user.Username'))
    Firstname = Column(String(30))
    Lastname = Column(String(30))
    Email = Column(String, unique=True)
    Password = Column(String(20))
    Phone = Column(Integer)


class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('user.User_ID'))
    Message = Column(String)
    Created_at = Column(Integer)


class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    Author_ID = Column(Integer, ForeignKey('user.User_ID'))
    Content = Column(String)
    post_id = Column(Integer, ForeignKey('post.ID'))


class Follower(Base):
    __tablename__ = 'follower'
    User_from_ID = Column(Integer, primary_key=True)
    User_to_ID = Column(Integer, ForeignKey('user.User_ID'))

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e