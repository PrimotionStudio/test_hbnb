#!/usr/bin/env python3
"""
    The saves a class object as a file
"""
import json

class Person:
    def __init__(self, name, age):
        if isinstance(name, str) and isinstance(age, int):
            self.name = name
            self.age = age
        else:
            raise TypeError("`name` must be of type `str` and `age` must be of type `str`")

    def __str__(self):
        return "[{}]: {{ [Name]: {} }}, {{ [Age]: {} }}".format(self.__class__.__name__, self.name, self.age)

    def save_to_json(self, filename="save_to_file.json"):
        with open(filename, "a") as f:
            json.dump(self.__dict__, f)
            f.write("\n")

    @classmethod
    def get_from_json(cls, filename="save_to_file.json"):
        instances = []
        with open(filename, "r") as f:
            line = f.readline().strip()
            while line:
                obj = json.loads(line)
                instances.append(cls(**obj))
                line = f.readline().strip()
        return instances

if __name__ == "__main__":
    """
    name = input("Name: ")
    age = int(input("Age: "))
    me = Person(name, age)
    print(me)
    me.save_to_json()
    """
    same = Person.get_from_json()
    print(same)
    print("[", end="")
    for i in same:
        print(i, end="")
    print("]", end="")
