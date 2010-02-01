#!/usr/bin/env python
"""Handles decoders"""
import config
import os
from glob import glob
import sys
import imp

#Decoders
decDir =  os.path.join(sys.path[0], "decoders")
files = glob(decDir + "/*.py")
files.remove(decDir + "/__init__.py")
modules = map(lambda m: imp.load_source(
        os.path.basename(os.path.splitext(m)[0]), m), files)

handlers = { }
for m in modules:
    for type in m.HANDLES:
        handlers[type] = m

def decode(inF, outF):
    """Decodes file inF to probably outF. outF is a hint as to where to decode
    to, but might not. Returns the filename that the file was decoded to."""
    type = os.path.splitext(inF)[1][1:].lower()
    if type in handlers:
        return handlers[type].decode(inF, outF)
    else:
        return None

def getMetadata(inF):
    type = os.path.splitext(inF)[1][1:].lower()
    if type in handlers:
        return handlers[type].getMetadata(inF)
    else:
        return None
