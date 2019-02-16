#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    isClass = ["BaseModel"]

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
        if len(args) == 0:
            print('** class name missing **')
        elif args not in self.isClass:
            print('** class doesn\'t exist **')
            return
        else:
            instance = eval("{}()".format(args))
            instance.save()
            print(instance.id)

    def do_show(self, args):
        ' prints str representation of an instance based on the class name and id'
        intake = args.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args not in self.isClass:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        
                show_me = storage.all()
                print(show_me[key])

    def do_destroy(self, args):
        'deletes an instance based on the class name and id'

    def do_all(self, args):
        'prints all str representation of all instances based or not on the class name'

    def do_update(self, args):
        'updates instance based on the class name and id by adding or updating attribute'

if __name__ == '__main__':
    HBNBCommand().cmdloop()
