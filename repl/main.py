#!/usr/bin/env python3
import signal
import sys
import cmd

class Repl(cmd.Cmd):
    prompt = "(hbnb) "
    def do_greet(self, person):
        """
        Usage: (Cmd) greet [person]
        Prints out `Hello, [person]` if the second argument is provided
        Prints out `Hello` if not
        """
        if person:
            print("Hello, {}".format(person))
        else:
            print("hello")

    _AVAILABLE = ('red', 'orange', 'yellow', 'green', 'blue')
    def complete_color(self, text, line, begidx, endidx):
        return [i for i in _AVAILABLE if i.startswith(text)]

    def help_introduction(self):
        print('introduction')
        print('a good place for a tutorial')

    def do_sqr(self, num):
        """
        Usage: (hbnb): sqr num
        prints out and returns a value which should cause the
        interpreter to exit
        """
        try:
            num = int(num)
        except TypeError:
            raise TypeError("num must be an int")

        print(num * num)
        return (num * num)

    def do_EOF(self, person):
        return True

def ctrlc(sig, handle):
    sys.exit(0)

def main():
    Repl().cmdloop()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, ctrlc)
    main()
