#!/usr/bin/env python3
"""
    This file reads a text file
"""
with open("test_file", encoding="utf-8") as f:
    i = 1
    line = f.readline()
    while (line):
        f.tell()
        print("Line {:d}: {}".format(i, line.strip()))
        i += 1
        line = f.readline()
