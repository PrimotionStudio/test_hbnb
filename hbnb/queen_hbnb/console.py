#!/usr/bin/python3
"""Module for HBNBCommand class"""

import re
from shlex import split
import cmd
from models import storage
from models.base_model import BaseModel


def parse(argument_string):
    """Parses an argument string, handling curly braces and brackets."""

    curly_brace_content_match = re.search(r"\{(.*?)}", argument_string)
    bracket_content_match = re.search(r"\[(.*?)]", argument_string)

    if curly_brace_content_match is None:
        if bracket_content_match is None:
            # No curly braces or brackets found, split on commas
            return [word.strip(",") for word in split(argument_string)]
        else:
            # Brackets found, handle separately
            lexer_output =\
                    split(argument_string[:bracket_content_match.span()[0]])
            parsed_elements = [word.strip(",") for word in lexer_output]
            parsed_elements.append(bracket_content_match.group())
            return parsed_elements
    else:
        # Curly braces found, handle separately
        lexer_output =\
                split(argument_string[:curly_brace_content_match.span()[0]])
        parsed_elements = [word.strip(",") for word in lexer_output]
        parsed_elements.append(curly_brace_content_match.group())
        return parsed_elements


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program by end of file"""
        print("")
        return True

    def emptyline(self):
        """Empty line handler to execute nothing"""
        pass

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel"""
        argument = parse(arg)
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argument[0])().id)
            storage.save()

    def do_show(self, arg):
        """Show command to print the string representation of an instance"""
        argument = parse(arg)
        obj_id = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif f"{argument[0]}.{argument[1]}" not in obj_id:
            print("** no instance found **")
        else:
            print(obj_id[f"{argument[0]}.{argument[1]}"])

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        argument = parse(arg)
        obj_destroy = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif f"{argument[0]}.{argument[1]}" not in obj_destroy.keys():
            print("** no instance found **")
        else:
            del (obj_destroy[f"{argument[0]}.{argument[1]}"])
            storage.save()

    def do_all(self, arg):
        """all command to print all string representation
        of all instances based or not on the class name
        """
        argument = parse(arg)
        if len(argument) > 0 and argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_all = []
            for obj in storage.all().values():
                if len(argument) > 0 and argument[0] ==\
                        obj.__class__.__name__:
                            obj_all.append(obj.__str__())
                elif len(argument) == 0:
                    obj_all.append(obj.__str__())
            print(obj_all)

    def do_update(self, arg):
        """Update command to update an instance"""
        argument = parse(arg)
        obj_update = storage.all()

        if len(argument) == 0:
            print("** class name missing **")
            return False
        if argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argument) == 1:
            print("** instance id missing **")
            return False
        if f"{argument[0]}.{argument[1]}" not in obj_update.keys():
            print("** no instance found **")
            return False
        if len(argument) == 2:
            print("** attribute name missing **")
            return False
        if len(argument) == 3:
            try:
                type(eval(argument[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argument) == 4:
            obj = obj_update[f"{argument[0]}.{argument[1]}"]
            if argument[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[argument[2]])
                obj.__dict__[argument[2]] = value_type(argument[3])
            else:
                obj.__dict__[argument[2]] = argument[3]
        elif type(eval(argument[2])) == dict:
            obj = obj_update[f"{argument[0]}.{argument[1]}"]
            for key, value in eval(argument[2]).items():
                if (key in obj.__class__.__dict__.keys()) and\
                        type(obj.__class__.__dict__[key] in {str, int, float}):
                            value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

