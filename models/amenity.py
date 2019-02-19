#!/usr/bin/python3
'''
class that inherits from basemodel
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    name: string -empty string
    '''
    name = ""

    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
