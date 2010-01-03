#!/usr/bin/env python
"Controls configuration"
import os

STATE=os.path.expanduser("~/.transcode")

def createState():
    "Makes sure the state directory exists"
    if not os.path.isdir(STATE):
        os.mkdir(STATE)

def cmdName(cmd):
    "Returns the name of the command of a module"
    return cmd.CMD
