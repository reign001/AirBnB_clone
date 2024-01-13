#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

=======
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
    
    
    
>>>>>>> aea2be03774243be0dea096a13bfe39b8345ac1f
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
<<<<<<< HEAD
=======
        
       
>>>>>>> aea2be03774243be0dea096a13bfe39b8345ac1f

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
<<<<<<< HEAD
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
=======
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
>>>>>>> aea2be03774243be0dea096a13bfe39b8345ac1f
