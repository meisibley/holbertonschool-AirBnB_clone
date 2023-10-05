#!/usr/bin/python3
# console.py
"""Defines the console for the AirBnB Clone Project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines a command interpreter for the AirBnB Clone

    Attributes:
        prompt (str): The command prompt to use
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Nothing happens if an empty line is received"""
        pass

    def do_quit(self):
        """Quit command to end the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal indicating to end the program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
