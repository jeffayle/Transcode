#!/usr/bin/env python
"""Handles decoders"""
import config
import os
from glob import glob
import sys
import imp

#Decoders
import flac
import mp3
import oggVorbis
import speex
import wave
import wavpack

modules = [flac, mp3, oggVorbis, speex, wave, wavpack]
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
