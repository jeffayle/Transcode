#!/usr/bin/env python
"""Handles decoding flac files"""
import subprocess

HANDLES=['flac','fla']

def decode(inF, outF):
    st = subprocess.call(["flac",
            "--totally-silent", #No output
            "--force", #Overwrite files
            "-o", outF, #Output
            inF #input
    ])

    if st == 0:
        return outF
    else:
        return False
