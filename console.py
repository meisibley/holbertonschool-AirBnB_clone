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

    def do_quit(self, arg):
        """Quit command to end the program"""
        return True

    def help_quit(self):
        """for help quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """EOF signal indicating to end the program"""
        return True

    def help_EOF(self):
        """for help EOF command"""
        print("EOF signal indicating to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
