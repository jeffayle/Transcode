#!/usr/bin/env python
"""Handles decoders"""
import config

#Decoders
import wave
handlers = { }
for m in [wave]:
    for type in m.HANDLES:
        handlers[type] = m
