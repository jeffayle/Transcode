#!/usr/bin/env python
"""Handles decoding wavpack files"""
import subprocess
import config

HANDLES=['wv']

def decode(inF, outF):
    ##TODO
    pass

def getTag(file, tag):
    p = subprocess.Popen(['wvunpack', '-q', '-x', tag, file],
            stdout=subprocess.PIPE)
    p.wait()
    output = p.communicate()[0]
    return output or None

def getMetaData(file):
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
