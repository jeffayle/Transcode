#!/usr/bin/env python
"""Handles decoding mp3 files"""
import subprocess
from .. import config

HANDLES=['mp3']

def decode(inF, outF):
    command = ['lame', '--decode']
    if config.quiet:
        command.append("--silent")
    command += [inF, outF]
    st = subprocess.call(command)

    if st == 0:
        return outF
    else:
        return False

getMetadata = config.readExiftoolMetadata
