#!/usr/bin/env python3
"""
    contains the entry point of the command interpreter:
"""
import cmd
import ast
# import sys
# import signal
from models.base_model import BaseModel
from models.user import User
from models import storage
from pprint import pprint


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = ["BaseModel", "User"]

    def emptyline(self):
        pass

    def do_EOF(self, hbnb):
        return True

    def do_quit(self, hbnb):
        return True

    def do_create(self, hbnb):
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
        """Print all instances of all or a certain class."""
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


def check_for_id(_id, obj_dict):
    for k, v in obj_dict.items():
        if v.to_dict()["id"] == _id:
            return (True)
    return (False)


def parse(value):
    try:
        parsed_value = ast.literal_eval(value)
        if isinstance(parsed_value, str):
            return parsed_value
    except (ValueError, SyntaxError):
        pass
    return value


def get_obj_from_id(_id, obj_dict):
    for k, v in obj_dict.items():
        if v.to_dict()["id"] == _id:
            return (v)
    return (False)

# def ctrlc(sig, handle):
#     sys.exit(0)

# signal.signal(signal.SIGINT, ctrlc)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
