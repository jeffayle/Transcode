#!/usr/bin/env python
"""Handles decoders"""
import config
import os

#Decoders
import wave
handlers = { }
for m in [wave]:
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
