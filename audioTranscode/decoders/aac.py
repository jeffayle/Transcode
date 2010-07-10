#!/usr/bin/env python
"""Handles decoding AAC files"""
import subprocess
from .. import config

HANDLES=['m4a','aac']

def decode(inF, outF):
    st = subprocess.call(['faad', '-o',outF, inF])
    if st == 0:
        return outF
    else:
        return False

getMetadata = config.readExiftoolMetadata
