# coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


try:
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    new_user = User(id='4', name='Jenny')
    session.add(new_user)
    session.commit()

    user = session.query(User).filter(User.id == 2).one()
    print('type: ', type(user))
    print('name: ', user.name)
finally:
    session.close()
