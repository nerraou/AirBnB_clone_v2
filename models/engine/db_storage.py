#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        username = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        database = os.getenv("HBNB_MYSQL_DB")
        host = os.getenv("HBNB_MYSQL_HOST")
        hbnb_env = os.getenv("HBNB_ENV")

        db_url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            username, password, host, database)

        self.__engine = create_engine(db_url, pool_pre_ping=True)
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

        # session = orm.Session(engine)

    def all(self, cls=None):
        """Returns all"""
        objects = {}

        if cls is None:
            classes = (User, State, City, Amenity, Place, Review)
            for class_type in classes:
                query = self.__session.query(class_type)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    objects[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                objects[obj_key] = obj

        return objects

    def save(self):
        """save changes to database"""
        self.__session.commit()

    def close(self):
        """Closes connection"""
        self.__session.close()

    def new(self, obj):
        """Adds new object to database"""
        if obj is not None:
            try:
                self.__session.add(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def delete(self, obj=None):
        """Removes an object from the database"""
        if obj is not None:
            obj_in_db = self.__session.query(type(obj)).filter(
                type(obj).id == obj.id)
            if obj_in_db is not None:
                obj_in_db.delete()

    def reload(self):
        """reload database"""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(SessionFactory)()
