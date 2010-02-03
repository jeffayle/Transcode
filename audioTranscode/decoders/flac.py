#!/usr/bin/env python
"""Handles decoding flac files"""
import subprocess
from .. import config

HANDLES=['flac','fla']

def decode(inF, outF):
    st = subprocess.call(["flac",
            ("--silent" if config.quiet else '--no-silent'), #No output
            "--decode", #Decode
            "--force", #Overwrite files
            "-o", outF, #Output
            inF #input
    ])

    if st == 0:
        return outF
    else:
        return False

getMetadata = config.readExiftoolMetadata
