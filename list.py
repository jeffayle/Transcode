#!/usr/bin/env python
"""Lists files to be processed
Usage: list"""
CMD="list"
import config
import os
import sys

def do():
    fn = os.path.join(config.STATE, "unprocessed")
    if os.path.isfile(fn):
        f = open(fn)
        sys.stdout.write(f.read())
        #Use stdout.write instead of print to not get extra linebreak
        f.close()
