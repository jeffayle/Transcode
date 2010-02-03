#!/usr/bin/env python
"""Handles decoding wavpack files"""
import subprocess
from .. import config

HANDLES=['wv']

def decode(inF, outF):
    options = [ 'wvunpack' ]
    if config.quiet:
        options.append("-q")
    options += [ '-y', inF, '-o', outF ]
    st = subprocess.call(options)

    if st == 0:
        return outF
    else:
        return False

def getTag(file, tag):
    p = subprocess.Popen(['wvunpack', '-q', '-x', tag, file],
            stdout=subprocess.PIPE)
    p.wait()
    output = p.communicate()[0]
    return output or None

def getMetadata(file):
    meta = { }
    meta['Title'] = getTag(file, "Title")
    meta['Artist'] = getTag(file, "Artist")
    meta['Album'] = getTag(file, "Album")
    meta['Genre'] = getTag(file, "Genre")
    meta['Track Number'] = getTag(file, "Track")
    meta['Tracktotal'] = getTag(file, "Tracktotal")
    meta['Date'] = getTag(file, "Year")

    for index in meta:
        if not meta[index]:
            del meta[index]
    return meta
