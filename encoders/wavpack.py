#!/usr/bin/env python
"""Handles encoding wavpack files"""
import subprocess
import config

HANDLES=['wv']

def encode(inF, outF, options, meta):
    #Get all options to send to wavpack
    cli_options = getCliOptions(inF, outF, options, meta)
    #Do the encoding
    st = subprocess.call(['wavpack'] + cli_options)

    if st == 0:
        return True
    else:
        return False

def getCliOptions(inF, outF, options, meta):
    "Build up a list of the the command line options to pass to wavpack"
    cli_options = [ ]
    if config.quiet:
        cli_options.append("-q") #Quiet mode
    cli_options.append("-y") #Say yes to warnings
    #Metadata
    if 'Title' in meta:
        cli_options.append("-w")
        cli_options.append("Title=%s"%meta['Title'])
    if 'Artist' in meta:
        cli_options.append("-w")
        cli_options.append("Artist=%s"%meta['Artist'])
    if 'Album' in meta:
        cli_options.append("-w")
        cli_options.append("Album=%s"%meta['Album'])
    if 'Genre' in meta:
        cli_options.append("-w")
        cli_options.append("Genre=%s"%meta['Genre'])
    if 'Track Number' in meta:
        cli_options.append("-w")
        cli_options.append("Track=%s"%meta['Track Number'])
    if 'Tracktotal' in meta:
        cli_options.append("-w")
        cli_options.append("Tracktotal=%s"%meta['Tracktotal'])
    if 'Date' in meta:
        cli_options.append("-w")
        cli_options.append("Year=%s"%meta['Date'])
    #Input and output file
    cli_options.append(inF)
    cli_options.append("-o")
    cli_options.append(outF)

    return cli_options
