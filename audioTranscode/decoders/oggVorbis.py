#!/usr/bin/env python
"""Handles decoding ogg vorbis files"""
import subprocess
import config

HANDLES=['ogg']

def decode(inF, outF):
    command = ['oggdec']
    if config.quiet:
        command.append("--quiet")
    command.append("--output=%s"%outF)
    command.append(inF)
    
    st = subprocess.call(command)
    
    if st == 0:
        return outF
    else:
        return False 

getMetadata = config.readExiftoolMetadata
