#!/usr/bin/env python3
"""
    Works with json
"""
import json
f = open("file.json", "r")
x = json.load(f)
print(x)
y = ["qwert", "fghjk", "sfghj"]
json.dumps(y)
