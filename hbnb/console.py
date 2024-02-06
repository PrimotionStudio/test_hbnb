#!/usr/bin/python3
"""
    contains the entry point of the command interpreter:
"""
import cmd
import ast
import sys
import signal
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from pprint import pprint


class HBNBCommand(cmd.Cmd):
    """
    The class that represents the Hotel Booking
    System Command Interpreter (CMD).
    """
    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "Place",
                 "State", "City", "Amenity", "Review"]

    def emptyline(self):
        """
        Overridden from Cmd base class to ignore empty lines.
        """
        pass

    def default(self, hbnb):
        """
        Prints an error message when a wrong command is entered.
        """
        line = hbnb
        hbnb = hbnb.split(".")
        if hbnb[0] in HBNBCommand.__classes:
            if hbnb[1] == "all()":
                self.do_all(hbnb[0])
            elif hbnb[1] == "count()":
                self.do_count(hbnb[0])
        else:
            self.stdout.write('*** Unknown syntax: %s\n' % line)

    def do_EOF(self, hbnb):
        """
        Exits the program on EOF.
        """
        return True

    def do_quit(self, hbnb):
        """
        Quit the hotel booking system CLI.
        """
        return True

    def do_create(self, hbnb):
        """
        Creates a new object instance for BaseModel
        or one of its subclasses.
        """
        hbnb = hbnb.strip()
        if hbnb:
            if hbnb in HBNBCommand.__classes:
                try:
                    new_bm = globals()[hbnb]()
                    new_bm.save()
                    print(new_bm.id)
                except KeyError:
                    print("** class doesn't exist **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, hbnb):
        """
        Show an existing object by ID.
        """
        hbnb = hbnb.strip()
        cmd_args = hbnb.split(" ")
        if not cmd_args[0]:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1 or not cmd_args[1]:
            print("** instance id missing **")
        elif not check_for_id(cmd_args[1], storage.all()):
            print("** no instance found **")
        else:
            try:
                print(storage.all()["<{}>.{}".format(
                    cmd_args[0], cmd_args[1])])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, hbnb):
        """
        Delete an existing object by ID.
        """
        hbnb = hbnb.strip()
        cmd_args = hbnb.split(" ")
        if not cmd_args[0]:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1 or not cmd_args[1]:
            print("** instance id missing **")
        elif not check_for_id(cmd_args[1], storage.all()):
            print("** no instance found **")
        else:
            try:
                del storage.all()["<{}>.{}".format(cmd_args[0], cmd_args[1])]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, hbnb):
        """
        Print all instances of all or a certain class.
        Usage: all [classname]
        """
        hbnb = hbnb.strip()
        obj_list = []
        if hbnb:
            if hbnb in HBNBCommand.__classes:
                for obj in storage.all().values():
                    if isinstance(obj, globals()[hbnb]):
                        obj_list.append(obj.__str__())
                print(obj_list)
            else:
                print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, hbnb):
        """
        Update the fields of an existing object by ID.
        Fields to update must be provided as key
        """
        hbnb = hbnb.strip()
        cmd_args = hbnb.split(" ")
        if not cmd_args[0]:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1 or not cmd_args[1]:
            print("** instance id missing **")
        elif not check_for_id(cmd_args[1], storage.all()):
            print("** no instance found **")
        elif len(cmd_args) == 2:
            print("** attribute name missing **")
        elif len(cmd_args) == 3:
            print("** value missing **")
        else:
            obj = get_obj_from_id(cmd_args[1], storage.all())
            setattr(obj, cmd_args[2].strip(), parse(cmd_args[3].strip()))
            storage.save()

    def do_count(self, hbnb):
        """
        """
        hbnb = hbnb.strip()
        pprint(globals())
        print(globals()[hbnb].__inst)


def check_for_id(_id, obj_dict):
    """
    Check if a given _id exists in a dictionary of objects
    """
    for k, v in obj_dict.items():
        if v.to_dict()["id"] == _id:
            return (True)
    return (False)


def parse(value):
    """
    Convert string input into appropriate
    Python data type based on its contents
    """
    try:
        parsed_value = ast.literal_eval(value)
        if isinstance(parsed_value, str):
            return parsed_value
    except (ValueError, SyntaxError):
        pass
    return value


def get_obj_from_id(_id, obj_dict):
    """
    Retrieve an object from the provided list
    of dictionaries using the "id" field as key
    """
    for k, v in obj_dict.items():
        if v.to_dict()["id"] == _id:
            return (v)
    return (False)


def ctrlc(sig, handle):
    """
    Handle Ctrl+C signal by printing out current
    state and exiting program gracefully
    """
    sys.exit(0)


signal.signal(signal.SIGINT, ctrlc)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
