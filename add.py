#!/usr/bin/env python
"""Adds files to be processed.
Usage: add [file1 [file2 [file3 [... filen]]]]"""
CMD="add"
import config
import os
import sys

def do():
    f = open(os.path.join(config.STATE,"unprocessed"), "a")
    for fn in sys.argv[2:]:
        addFile(f, fn)

def addFile(buff, fname):
    "Adds a file to be processed"
    ##TODO: Add directories recursively
    ##TODO: Check if file exists before adding
    buff.write("%s\n"%(fname))
