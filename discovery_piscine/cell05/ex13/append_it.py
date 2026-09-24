#!/usr/bin/env python3
import sys
import re

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for param in params:
        if not re.search(r'ism$', param):
            print(f"{param}ism")
