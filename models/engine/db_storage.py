#!/usr/bin/python3
""" DBStorage """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """ Class DBStorage """
    __engine = None
    __session = None

    def __init__(self):
        """ Init dbStorage """
        db_user = getenv('HBNB_MYSQL_USER')
        db_pwd = getenv('HBNB_MYSQL_PWD')
        db_host = getenv('HBNB_MYSQL_HOST')
        db_db = getenv('HBNB_MYSQL_DB')
        db_env = getenv('HBNB_ENV')

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                db_user, db_pwd, db_host, db_db), pool_pre_ping=True)

        if db_env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Return and show all class obj DBstorage """
        my_dyct = {}
        if cls is None:
            for table in [City, State, User, Place, Amenity, Review]:
                for instance in self.__session.query(table).all():
                    my_dyct["{}.{}".format(
                       table, instance.id)] = instance

        else:
            for instance in self.__session.query(eval(cls)).all():
                my_dyct["{}.{}".format(
                    eval(cls).__name__, instance.id)] = instance

        return my_dyct

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database sessio """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Create all table of session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ Close and delete session """
        self.__session.close()
