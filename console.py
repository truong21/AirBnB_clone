#!/usr/bin/python3
import cmd
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
<<<<<<< HEAD


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    isClass = ["BaseModel", "User", "City", "Amenity", "Review",
               "State", "Place"]
=======
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    isClass = ["BaseModel", "User", "City", "Amenity",
               "Review", "State","Place"]
>>>>>>> a632790d4f5e84512895dbfccb1813c6f4b34095

    def do_quit(self, args):
        '''exit the program'''
        exit()

    def do_EOF(self, args):
        '''exit the program'''
        return True

    def emptyline(self):
        '''dosent execute when line is empty'''
        pass

    def do_create(self, args):
        """ creates a new instance of BaseModel, saves it to json,
            &prints the id
        """
        argv = args.split()
        if len(argv) == 0:
            print('** class name missing **')
        elif argv[0] not in self.isClass:
            print("** class doesn't exist **")
        else:
            instance = eval("{}()".format(argv[0]))
            instance.save()
            print(instance.id)

    def do_show(self, line):
<<<<<<< HEAD
        ' prints str representation of an instance based on the class\
        name and id'
        intake = line.split()
        print(intake)
=======
        """ prints str representation of an instance based on the class
        name and id
        """
        intake = line.split()
>>>>>>> a632790d4f5e84512895dbfccb1813c6f4b34095
        if len(intake) == 0:
            print('** class name missing **')
        elif intake[0] not in self.isClass:
            print("** class doesn't exist **")
        elif len(intake) < 2:
<<<<<<< HEAD
            print('** instance id missing **')
            return
        key = str(intake[0]) + '.' + str(intake[1])
        showme = storage.all()
        print(showme[key])

=======
            print("** instance id missing **")
        else:
            showme = storage.all()
            key = str(intake[0]) + '.' + str(intake[1])
            if key in showme:
                print(showme[key])
            else:
                print("** no instance found **")
         
>>>>>>> a632790d4f5e84512895dbfccb1813c6f4b34095
    def do_destroy(self, args):
        """ deletes an instance based on the class name and id,
            but saves the changes in JSON file
        """
        argv = args.split()
        if len(argv) == 0:
            print('** class name missing **')
        elif argv[0] not in self.isClass:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            showme = storage.all()
            key = str(argv[0]) + '.' + str(argv[1])
            if key in showme:
                del showme[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
<<<<<<< HEAD
        'prints all str representation of all instances based or\
        not on the class name'

    def do_update(self, args):
        'updates instance based on the class name and id by adding or\
        updating attribute'
=======
        """"prints all str representation of all instances based or not
            on the class name
        """
        showme = storage.all()
        objs_list = []
        if not args:
            for key, obj in showme.items():
                objs_list.append(str(obj))
            print(objs_list)
        else:
            argv = args.split()
            if argv[0] not in self.isClass:
                print("** class doesn't exist **")
            else:
                for key, obj in showme.items():
                    instance = obj.to_dict()
                    if instance['__class__'] == argv[0]:
                        objs_list.append(str(showme[key]))
                print(objs_list)

    def do_update(self, args):
        """ updates instance based on the class name and id by adding or
            updating attribute
        """
        argv = args.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] not in self.isClass:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif len(argv) == 2:
            print("** attribute name missing **")
        elif len(argv) == 3:
            print("** value missing **")
        else:
            showme = storage.all()
            key = str(argv[0]) + '.' + str(argv[1])
            if key in showme:
                setattr(showme[key], argv[2], argv[3])
                storage.save()
            else:
                print("** no instance found **")

>>>>>>> a632790d4f5e84512895dbfccb1813c6f4b34095

if __name__ == '__main__':
    HBNBCommand().cmdloop()
