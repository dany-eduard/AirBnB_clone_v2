#!/usr/bin/python3
'''
    Declaration for database storage
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session, exc
import os

clases={"State": State, "City": City, "User": User,
        "Place": Place, "Review": Review, "Amenity": Amenity}

class DBStorage():
    __engine = None
    __session = None
    def __init__(self):
        """init method of DBStorage"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        localhost = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB', default=None)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}}/{}'.format(
            user, password, localhost, db_name), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metada.drop_all(self.__engine)
        
    def all(self, cls=None):
        """
        all of DBStorage
        """
        dbstore = {}
        if cls:
            if type(cls) is str and cls in clases:
                for obj in self.__session.query(clases[cls]).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    dbstore[key] = val
            elif cls.__name__ in clases:
                for obj in self.__session.query(cls).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    val = obj
                    dbstore[key] = val
        else:
            for k, v in clases.items():
                for obj in self.__session.query(v).all():
                    key = str(v.__name__) + "." + str(obj.id)
                    val = obj
                    dbstore[key] = val
        return dbstore
    
    def new(self, obj):
        """
        add new object to database session
        """
        if obj:
            self.__session.add(obj)
    
    def save(self):
        """
        commit the changes of the current database session
        """
        self.__session.commit()
        
    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Close method """
        self.__session.close()
