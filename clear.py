#!/usr/bin/env python
"""Clears the list of files to be processed
Usage: clear [y]
If 'y' is not the third command line argument, user will be asked for
confirmation"""
CMD="clear"
import config
import os
import sys

def do():
    fn = os.path.join(config.STATE, "unprocessed")
    confirmed = False
    if len(sys.argv)>=3 and sys.argv[2] == 'y':
        confirmed = True
    else:
        confirmed = raw_input("Clear unprocessed files? [yn] ")=='y'
    ###
    if confirmed:
        os.unlink(os.path.join(config.STATE, "unprocessed"))
