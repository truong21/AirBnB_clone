#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, args):
        'exit the program'
        exit()

    def do_EOF(self, line):
        'exit the program'
        return True

    def emptyline(self):
        'dosent execute when line is empty'
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
