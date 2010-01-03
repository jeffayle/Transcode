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
    f.close()

def addFile(buff, fname):
    "Adds a file to be processed"
    fname = os.path.realpath(fname) #Expand path
    if os.path.isfile(fname):
        buff.write("%s\n"%(fname))
        print "Added '%s'"%(fname)
    elif os.path.isdir(fname):
        for fn in filter(lambda s: s[0]!='.', os.listdir(fname)):
            #Recurse into non dot files/directories
            addFile(buff, fn)
    else:
        sys.stderr.write("File not found '%s'\n"%(fname))
