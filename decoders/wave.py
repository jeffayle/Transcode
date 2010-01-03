#!/usr/bin/env python
"""Handles decoding wav files
**Does not actually do anything, wav files are already decoded as far as we're
concerned"""
HANDLES=['wav']

def decode(inF, outF):
    return inF

def getMetadata(inF):
    return {} #wavs don't carry any metadata
