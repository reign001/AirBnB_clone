#!/usr/bin/python3
import models
from datetime import *
import uuid


class BaseModel:
    """this class handles the database of the Hbnb project"""
    
    def __init__(self, *args, **kwargs):
        """this initializes a new base models
        ARGS:
            *args: unlimited positional arguments
            **kwargs (dict): key/value pairs
        """
        timeForm = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(**kwargs) != 0:
            for L, M in kwargs.items():
                if L == "created_at" or L == "updated_at":
                    self.__dict__[L] = datetime.strptime(M, timeForm)
                else:
                    self.__dict__[L] = M
        else:
            models.storage.save()                
    
    def save(self):
        """this updates the updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()
    
    
    
    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
        
       

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)