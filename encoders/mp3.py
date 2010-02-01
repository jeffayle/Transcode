#!/usr/bin/env python
"""Handles encoding mp3 files"""
import subprocess

HANDLES=["mp3"]

def encode(inF, outF, options, metadata):
    #Get the options to send to lame
    cli_options = getCliOptions(inF, outF, options, metadata)
    #Do the encoding
    st = subprocess.call(['lame'] + cli_options)

    if st == 0:
        return True
    else:
        return False

def getCliOptions(inF, outF, options, meta):
    "Builds up a list of command line options to pass to lame"
    cli_options = [ ]
    cli_options.append("--silent") #no output
    cli_options.append("--add-id3v2") #Make sure v2 tags are written
    #Metadata
    if 'Title' in meta:
        cli_options.append("--tt")
        cli_options.append(meta['Title'])
    if 'Artist' in meta:
        cli_options.append("--ta")
        cli_options.append(meta['Artist'])
    if 'Album' in meta:
        cli_options.append("--tl")
        cli_options.append(meta['Album'])
    if 'Genre' in meta:
        cli_options.append("--tg")
        cli_options.append(meta['Genre'])
    if 'Track Number' in meta and 'Tracktotal' in meta:
        cli_options.append("--tn")
        cli_options.append("%s/%s"%(meta['Track Number'], meta['Tracktotal']))
    elif 'Track Number' in meta:
        cli_options.append("--tn")
        cli_options.append(meta['Track Number'])
    elif 'Date' in meta:
        cli_options.append("--ty")
        cli_options.append(meta['Date'])
    #User options
    cli_options += options
    #Input and output file
    cli_options.append(inF)
    cli_options.append(outF)

    return cli_options
