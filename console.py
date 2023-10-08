#!/usr/bin/python3
# console.py
"""Defines the console for the AirBnB Clone Project"""
import cmd
import re
from shlex import split
from models import storage


def sep(arg):
    c_brackets = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if c_brackets is None:
        if brackets is None:
            return [t_args.strip(",") for t_args in split(arg)]
        else:
            index = split(arg[:brackets.span()[0]])
            new_args = [t_args.strip(",") for t_args in index]
            new_args.append(brackets.group())
            return new_args
    else:
        index = split(arg[:c_brackets.span()[0]])
        new_args = [t_args.strip(",") for t_args in index]
        new_args.append(c_brackets.group())
        return new_args


class HBNBCommand(cmd.Cmd):
    """Defines a command interpreter for the AirBnB Clone

    Attributes:
        prompt (str): The command prompt to use
        __classes (set): The actionable classes
    """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
    }

    def emptyline(self):
        """Nothing happens if an empty line is received"""
        pass

    def do_quit(self, *args):
        """Quit command to end the program"""
        return True

    def help_quit(self):
        """for help quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, *args):
        """EOF signal indicating to end the program"""
        print("")
        return True

    def help_EOF(self):
        """for help EOF command"""
        print("EOF signal indicating to exit the program\n")

    def do_create(self, arg):
        """Creates a new instance of given class"""
        args1 = sep(arg)
        if len(args1) == 0:
            print("** class name missing **")
        elif args1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args1[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints str rep of id in the named class"""
        args1 = sep(arg)
        obj_dict = storage.all()
        if len(args1) == 0:
            print("** class name missing **")
        elif args1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args1[0], args1[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args1[0], args1[1])])

    def do_destroy(self, arg):
        """Deletes an instance of class.id and saves"""
        args1 = sep(arg)
        obj_dict = storage.all()
        if len(args1) == 0:
            print("** class name missing **")
        elif args1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args1[0], args1[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args1[0], args1[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all str rep of given class, or all available"""
        args1 = sep(arg)
        if len(args1) > 0 and args1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            ob1 = []
            for obj in storage.all().values():
                if len(args1) > 0 and args1[0] == obj.__class__.__name__:
                    ob1.append(obj.__str__())
                elif len(args1) == 0:
                    ob1.append(obj.__str__())
            print(ob1)

    def do_update(self, arg):
        """Updates/Adds a single attribute to obbject"""
        args1 = sep(arg)
        obj_dict = storage.all()
        if len(args1) == 0:
            print("** class name missing **")
            return False
        elif args1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        elif len(args1) == 1:
            print("** instance id missing **")
            return False
        elif "{}.{}".format(args1[0], args1[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        elif len(args1) == 2:
            print("** attribute name missing **")
            return False
        if len(args1) == 3:
            try:
                type(eval(args1[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args1) == 4:
            new_obj = obj_dict["{}.{}".format(args1[0], args1[1])]
            if args1[2] in new_obj.__class__.__dict__.keys():
                v_type = type(new_obj.___class__.__dict__[args1[2]])
                new_obj.__dict__[args1[2]] = v_type(args1[3])
            else:
                new_obj.__dict__[args1[2]] = args1[3]
        elif type(eval(args1[2])) == dict:
            ob = obj_dict["{}.{}".format(args1[0], args1[1])]
            for k, v in eval(args1[2]).items():
                if (k in ob.__class__.__dict__[k].keys() and
                    type(ob.__class__.__dict__[k]) in {str,
                                                       int, float}):
                    v_type = type(ob.__class__.__dict__[k])
                    ob.__dict__[k] = v_type(v)
                else:
                    ob.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
