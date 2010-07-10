#!/usr/bin/env python
"Controls configuration"
import os
import subprocess

quiet = False

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
    data = dict(data)

    #MP3 track shows up as 'Track' and not 'Track Number'
    if data.has_key('Track'):
        data['Track Number'] = data['Track']
    #Flac is showing 'Tracknumber' for 'Track Number'
    if data.has_key('Tracknumber'):
        data['Track Number'] = data['Tracknumber']
    #Split track number if it has a slash in it
    if (data.has_key('Track Number'))and('/' in data['Track Number']):
        data['Track Number'],data['Tracktotal'] = \
                data['Track Number'].split('/')
    #Same for for 'of'
    if (data.has_key('Track Number'))and(' of ' in data['Track Number']):
        data['Track Number'],data['Tracktotal'] = \
                data['Track Number'].split(' of ')

    return data
