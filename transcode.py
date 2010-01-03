#!/usr/bin/env python
import config
import sys

#Commands
import add
import list
commands = [
    add,
    list
]

config.createState()

#Check arguments
if len(sys.argv) >= 2:
    command = sys.argv[1]
else:
    command = None

#Do that command
if command:
    if command in map(config.cmdName, commands):
        #do() that command
        filter(lambda a: config.cmdName(a)==command,commands)[0].do()
    else:
        sys.stderr.write("Unknown command '%s'\n"%(command))
else:
    sys.stderr.write("Usage: %s <command> [arguments]\n"%(sys.argv[0]))
