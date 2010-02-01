#!/usr/bin/env python
"""Handles encoding flac files"""
import subprocess
import config

HANDLES=['flac','fla']
DEFTYPE='flac'

def encode(inF, outF, options, metadata):
    print "Encoding to flac..."
