#!/usr/bin/env python3

'''
Python script to check if file or directory.

all shell scripts MUST start with sha-bang on the FIRST LINE.
since it uses '#!' we don't have type 'python3 filename.py' only
'filename.py' be sure .py file has executable permission (chmod +x)

this program is more like a  shell script and less like a program (easy2.py)

demos:
    *using python built-in functions for working with the OS.


usage: file_or_dir.py path
'''

import os
from sys import argv

# must be exactly 2 args: the filename and path.
if len(argv) != 2:
    print("usage: %s path" % (argv[0]))

path = argv[1]

if os.path.isdir(path):
    print(path, "is a directory.")
elif os.path.isfile(path):
    print(path, "is a file.")
else:
    print(path, "is not a file or directory.")
    #might be a socket, but sockets are just special type of files.
    #are pipes a socket too? are they a type of file?
