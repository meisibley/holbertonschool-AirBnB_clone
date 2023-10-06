#!/usr/bin/python3
# console.py
"""Defines the console for the AirBnB Clone Project"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines a command interpreter for the AirBnB Clone

    Attributes:
        prompt (str): The command prompt to use
    """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "user",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
    }

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
        print("")
        return True

    def help_EOF(self):
        """for help EOF command"""
        print("EOF signal indicating to exit the program\n")

    def do_create(self, name):
        """Creates a new instance of given class

        Args:
            name (str): The name of the class to create
        """
        if not name:
            print("** class name missing **")
        elif name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(name)().id)
            storage.save()

    def do_show(self, name, iden):
        """Prints str rep of id in the named class

        Args:
            name (str): The class name to be used
            iden (str): THe id of the obj to print
        """
        obj_dict = storage.all()
        if not name:
            print("** class name missing **")
        elif name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif not iden:
            print("** instance id missing **")
        elif "{}.{}".format(name, iden) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(name, iden)])

    def do_destroy(self, name, iden):
        """Deletes an instance of name.iden and saves

        Args:
            name (str): The class name
            iden (str): The id of the instance
        """
        obj_dict = storage.all()
        if not name:
            print("** class name missing **")
        elif name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif not iden:
            print("** instance id missing **")
        elif "{}.{}".format(name, iden) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(name, iden)]
            storage.save()

    def do_all(self, name):
        """Prints all str rep of given class, or all available

        Args:
            name (str): (optional) Class to print
        """
        if name and name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for obj in storage.all().values():
                if name and name == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                else:
                    obj1.append(obj.__str__())
            print(obj1)

    def do_update(self, name, iden, attr, value):
        """Adds a single attribute to the given instance

        Args:
            name (str): The name of the class
            iden (str): The instance to update
            attr (str): The attribute to add
            value (any): The vaue of attr
        """
        obj_dict = storage.all()
        if not name:
            print("** class name missing **")
        elif name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif not iden:
            print("** instance id missing **")
        elif "{}.{}".format(name, iden) not in obj_dict:
            print("** no instance found **")
        elif not attr:
            print("** attribute name missing **")
        elif not value:
            print("** value missing **")
        else:
            obj1 = obj_dict["{}.{}".format(name, iden)]
            if attr in obj1.__class__.__dict__.keys():
                v_type = type(obj1.__class__.__dict__[attr])
                obj1.__dict__[attr] = v_type(value)
            else:
                obj1.__dict__[attr] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
