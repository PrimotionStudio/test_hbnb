#!/usr/bin/env python3
import signal
import sys

def ctrlc(sig, handle):
    sys.exit(0)

def execute(cmd):
    print("{}: command not found".format(cmd))

def main():
    while True:
        cmd = input("(hbnh) ")
        if cmd.strip() == "quit":
            break
        elif cmd.strip() == "help":
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF help quit")
        elif cmd.strip() == "":
            continue
        else:
            execute(cmd)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, ctrlc)
    main()
