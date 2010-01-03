#!/usr/bin/env python
"Controls configuration"
import os
import subprocess

STATE=os.path.expanduser("~/.transcode")

def createState():
    "Makes sure the state directory exists"
    if not os.path.isdir(STATE):
        os.mkdir(STATE)

def cmdName(cmd):
    "Returns the name of the command of a module"
    return cmd.CMD

#Thanks to Mark Byers
#http://stackoverflow.com/questions/1993840/map-list-onto-dictionary/1993853
def mapDict(keyFunction, values):
    "Maps a list onto a dictionary. Return value of keyFunction is used as \
    the key, value is the original value"
    return dict((keyFunction(v), v) for v in values)

def readExiftoolMetadata(file):
    "Uses exiftool to read metadata from a file, returns a dictionary"
    p = subprocess.Popen(["exiftool",file], stdout=subprocess.PIPE)
    p.wait() #Wait for it to finish
    output = p.communicate()[0]
    #Split on linebreaks, then on spaces, stripping extra whitespace
    data = map(lambda ln: map(str.strip, ln.split(":",1)), output.split("\n"))
    data.remove(['']) #Remove blank list
    return dict(data)
