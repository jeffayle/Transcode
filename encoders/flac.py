#!/usr/bin/env python
"""Handles encoding flac files"""
import subprocess
import config

HANDLES=['flac','fla']

def encode(inF, outF, options, metadata):
    #Get all the options to give to flac
    cli_options = getCliOptions(inF, outF, options, metadata)
    #Do the actual encoding
    st = subprocess.call(['flac'] + cli_options)

    if st == 0:
        return True
    else:
        return False
    
def getCliOptions(inF, outF, options, metadata):
    "Builds up a list of the command line options to pass to flac"
    cli_options = [ ]
    cli_options.append("--output-name=%s"%outF) #Output file
    cli_options.append("--totally-silent") #No output
    cli_options.append("--force") #Overwrite existing files
    #Metadata
    if 'Title' in metadata:
        cli_options.append("--tag=title=%s"%metadata['Title'])
    if 'Artist' in metadata:
        cli_options.append("--tag=artist=%s"%metadata['Artist'])
    if 'Album' in metadata:
        cli_options.append("--tag=album=%s"%metadata['Album'])
    if 'Genre' in metadata:
        cli_options.append("--tag=genre=%s"%metadata['Genre'])
    if 'Track Number' in metadata:
        cli_options.append("--tag=tracknumber=%s"%metadata['Track Number'])
    if 'Date' in metadata:
        cli_options.append("--tag=date=%s"%metadata['Date'])
    #Add user's options
    cli_options += options
    #Add input file
    cli_options.append(inF)

    return cli_options
