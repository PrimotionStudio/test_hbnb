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

    def do_quit(self, input_command):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, input_command):
        """Quit command to exit the program by end of file"""
        print("")
        return True

    def emptyline(self):
        """Empty line handler to execute nothing"""
        pass

    def do_create(self, input_command):
        """Create command to create a new instance of BaseModel"""
        argument = parse(input_command)
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

    def do_destroy(self, input_command):
        """Destroy command to delete an instance"""
        argument = parse(input_command)
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

    def do_all(self, input_command):
        """all command to print all string representation
        of all instances based or not on the class name
        """
        argument = parse(input_command)
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

    def do_update(self, input_command):
        """Update command to update an instance"""
        argument = parse(input_command)
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

    def do_count(self, input_command):
        """
        Prints the number of instances of a given class.

        Args:
            input_command (str): The argument provided by the user,
            either the class name or class name with .count().

        If the argument contains only the class name,
        it counts the instances directly.
        If the argument includes .count(), it counts the instances
        using a class method.
        """
        argument = parse(input_command)
        count = 0
        for obj in storage.all().values():
            if argument[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, input_command):
        """
        Default behavior for the command interpreter
        when the input command is invalid.

        Args:
            input_command (str): The input command provided by the user.

        Returns:
            bool: False if the input command is invalid,
            otherwise executes the appropriate command.

        Invoked when the provided command does not match
        any of the predefined commands.
        It attempts to parse the input command and execute
        the corresponding action if possible.

        If the input command matches the expected syntax,
        it extracts the sub-command and arguments,
        then executes the corresponding action using the command map.

        If the input command does not match the expected syntax or
        the sub-command is not recognized,
        it prints an error message and returns False.
        """
        command_map = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }

        match = re.search(r"\.", input_command)
        if match is not None:
            command_split = [input_command[:match.span()[0]],
                             input_command[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", command_split[1])
            if match is not None:
                sub_command = [command_split[1][:match.span()[0]],
                               match.group()[1:-1]]
                if sub_command[0] in command_map.keys():
                    full_command = "{} {}".format(command_split[0],
                                                  sub_command[1])
                    return command_map[sub_command[0]](full_command)

        print("*** Unknown syntax: {}".format(input_command))
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
