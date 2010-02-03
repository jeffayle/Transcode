#!/usr/bin/env python
"""Handles encoding ogg speex files"""
import subprocess
from .. import config

HANDLES=['spx']

def encode(inF, outF, options, meta):
    #Get the command line options to pass to speexenc
    cli_options = getCliOptions(inF, outF, options, meta)
    #Run the encoder
    if config.quiet:
        stderr = open("/dev/null", "w")
    else:
        stderr = None
    st = subprocess.call(['speexenc'] + cli_options, stderr=stderr)

    if st == 0:
        return True
    else:
        return False

def getCliOptions(inF, outF, options, meta):
    cli_options = [ ]
    if 'Title' in meta:
        cli_options.append('--title')
        cli_options.append(meta['Title'])
    if 'Artist' in meta:
        cli_options.append('--author')
        cli_options.append(meta['Artist'])
    #Add user's options
    cli_options += options
    #input/output files
    cli_options.append(inF)
    cli_options.append(outF)

    return cli_options
