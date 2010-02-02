#!/usr/bin/env python
"""Handles encoding ogg vorbis files"""
import subprocess
import config

HANDLES=['ogg']

def encode(inF, outF, options, meta):
    #Get all the options to give to oggenc
    cli_options = getCliOptions(inF, outF, options, meta)
    #Do the actual encoding
    st = subprocess.call(['oggenc'] + cli_options)

    if st == 0:
        return True
    else:
        return False

def getCliOptions(inF, outF, options, meta):
    "Build up a list of options to pass to oggenc"
    cli_options = [ ]
    cli_options.append("--output=%s"%outF) #Output file
    if config.quiet:
        cli_options.append("--quiet") #No output
    #Metadata
    if 'Title' in meta:
        cli_options.append("--title")
        cli_options.append(meta['Title'])
    if 'Artist' in meta:
        cli_options.append("--artist")
        cli_options.append(meta['Artist'])
    if 'Album' in meta:
        cli_options.append("--album")
        cli_options.append(meta['Album'])
    if 'Genre' in meta:
        cli_options.append("--genre")
        cli_options.append(meta['Genre'])
    if 'Track Number' in meta:
        cli_options.append("--tracknum")
        cli_options.append(meta['Track Number'])
    if 'Date' in meta:
        cli_options.append("--date")
        cli_options.append(meta['Date'])
    #User options
    cli_options += options
    #Input file
    cli_options.append(inF)

    return cli_options
