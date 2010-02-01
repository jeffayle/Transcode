#!/usr/bin/env python
"""Handles encoders"""
import config
import os
from glob import glob
import sys
import imp

#Encoders
encDir = os.path.join(sys.path[0], "encoders")
files = glob(encDir + "/*.py")
files.remove(encDir + "/__init__.py")
modules = map(lambda m: imp.load_source(
        os.path.basename(os.path.splitext(m)[0]), m), files)

handlers = { }
for m in modules:
    for type in m.HANDLES:
        handlers[type] = m

def encode(inF, outF, type, options, metadata):
    """Encodes inF to outF with given options and metadata"""
    if type in handlers:
        return handlers[type].encode(inF, outF, options, metadata)
    else:
        return None
