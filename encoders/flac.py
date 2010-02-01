#!/usr/bin/env python
"""Handles encoding flac files"""
import subprocess
import config

HANDLES=['flac','fla']
DEFTYPE='flac'

def encode(inF, outF, options, metadata):
    cli_options = [ ]
    cli_options.append("--output-name=%s"%outF) #Output file
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

    return cli_options
