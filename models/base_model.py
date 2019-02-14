#!/usr/bin/python3
'''
BaseModel class that will be used by all instances
'''
import models
from datetime import datetime
import uuid

class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    def __str__(self):
        return("[{}] [{}] [{}]".format(self.__class__.__name__, self.id, self.__dict__))


    def save(self):
        '''updates updated_at with current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns dict containing all key values of __dict__'''
        instance = self.__dict__.copy()
        instance['__class__'] = self.__class__.__name__
        instance['created_at'] = self.created_at.isoformat()
        instance['updated_at'] = self.updated_at.isoformat()
        return instance
