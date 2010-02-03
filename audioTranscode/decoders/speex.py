#!/usr/bin/env python
"""Handles decoding speex files"""
import config
import subprocess

HANDLES=['spx']

def decode(inF, outF):
    if config.quiet:
        stderr = open("/dev/null", "w")
    else:
        stderr = None
    st = subprocess.call(['speexdec',inF,outF], stderr=stderr)

    if st == 0:
        return outF
    else:
        return False

def getMetadata(file):
    return { }
