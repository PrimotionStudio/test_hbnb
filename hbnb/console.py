#!/usr/bin/env python3
"""
    contains the entry point of the command interpreter:
"""
import cmd
# import sys
# import signal
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = ["BaseModel"]

    def emptyline(self, hbnb):
        pass

    def do_EOF(self, hbnb):
        return True

    def do_quit(self, hbnb):
        return True

    def do_create(self, hbnb):
        if hbnb:
            if hbnb in HBNBCommand.__classes:
                new_bm = BaseModel(hbnb)
                new_bm.save()
                print(new_bm.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, hbnb):
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
            print(storage.all()["<{}>.{}".format(cmd_args[0], cmd_args[1])])

    def do_destroy(self, hbnb):
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
            del storage.all()["<{}>.{}".format(cmd_args[0], cmd_args[1])]
            storage.save()


def check_for_id(_id, obj_dict):
    for k, v in obj_dict.items():
        if v.to_dict()["id"] == _id:
            return (True)
    return (False)

# def ctrlc(sig, handle):
#     sys.exit(0)


if __name__ == "__main__":
    # signal.signal(signal.SIGINT, ctrlc)
    HBNBCommand().cmdloop()
