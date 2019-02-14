#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    isClass = {'BaseClass'}

    def do_quit(self, args):
        'exit the program'
        exit()

    def do_EOF(self, args):
        'exit the program'
        return True

    def emptyline(self):
        'dosent execute when line is empty'
        pass

    def do_create(self, args):
        'creates a new instance of BaseModel, saves it to json, &prints the id'
        if (isClass):
            instance = BaseModel()
            print(self.id)
        else:
            print ('** class dosent exist**')

    def do_show(self, args):
        ' prints str representation of an instance based on the class name and id'

    def do_destroy(self, args):
        'deletes an instance based on the class name and id'

    def do_all(self, args):
        'prints all str representation of all instances based or not on the class name'

    def do_update(self, args):
        'updates instance based on the class name and id by adding or updating attribute'

if __name__ == '__main__':
    HBNBCommand().cmdloop()
