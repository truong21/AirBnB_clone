#!/usr/bin/python3
'''
inherits from basemodel class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    '''
    state_id = ""
    name = ""
