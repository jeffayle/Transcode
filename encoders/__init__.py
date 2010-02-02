#!/usr/bin/env python
"""Handles encoders"""
import config
import os
from glob import glob
import sys
import imp

#Encoders
import flac
import mp3
import oggVorbis
import speex
import wavpack

modules = [flac, mp3, oggVorbis, speex, wavpack]
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
