#!/usr/bin/python3
'''
FileStorage seralizes instances to JSON file and deseralizes fils to instances
'''
import json
import models

class FileStorage()
    '''
    serializes instances to a JSON file and deserializes JSON file to instances

    __file_path: path to JSON file
    __objects: empty dictionary that will store all objects

    '''
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        '''
        returns the dictionary __objects
        '''
        return (self.__objects)

    def new(self,obj):
        '''
        sets in __objects the obj key
        '''
        self.__objects["{} {}".format(obj.__class__.__name__, obj.id) = obj
    def save(self):
        '''
        serializes __objects to JSON file path
        '''
        cereal = {}
        with open(self.__file_path, 'w') as c_file:
            for key in self.__objects.items
            json.dump(self.__objects, c_file)

    def reload(self):
        '''
        desearializes the JSON file to __objects
        '''
        if (self.__file_path):
            with open(self.__file_path, 'r') as r_file:
                return json.load(r_file)
        else:
            return


