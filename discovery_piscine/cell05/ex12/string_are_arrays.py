#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    z_list = [char for char in sys.argv[1] if char == 'z']
    if z_list:
        print("".join(z_list))
    else:
        print("none")
