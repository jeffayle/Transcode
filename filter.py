#!/usr/bin/python
"""Filter the list of files to be processed. Removes all duplicates, then
applies regular expression.
Usage: filter [pattern]
Pattern is a regular expression to check files against, if it is not given
all files will pass."""
CMD="filter"

import config
import os
import re
import sys

def do():
    fn = os.path.join(config.STATE, "unprocessed")
    if os.path.exists(fn):
        files = set(open(fn).read().splitlines())
    else:
        return #There are no files queued
    ###
    if len(sys.argv) >= 3:
        pattern = sys.argv[2]
    else:
        pattern = '.'
    ###
    rePattern = re.compile(pattern)
    newfiles = filter(lambda a: re.search(rePattern, a), files)
    os.unlink(fn)
    f = open(fn, "w")
    for file in newfiles:
        f.write("%s\n"%(file))
    f.close()
