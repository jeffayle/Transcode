#!/usr/bin/env python
import config
import sys

#Commands
import add
import list
import clear
commands = config.mapDict(config.cmdName, [
    add,
    list,
    clear
])

config.createState()

#Check arguments
if len(sys.argv) >= 2:
    command = sys.argv[1]
else:
    command = None

#Do that command
if command:
    if command in commands:
        #do() that command
        commands[command].do()
    else:
        sys.stderr.write("Unknown command '%s'\n"%(command))
else:
    sys.stderr.write("Usage: %s <command> [arguments]\n"%(sys.argv[0]))
