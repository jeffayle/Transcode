#!/usr/bin/env python
import encoders
import decoders
import config
import tempfile
import os

def transcode(inF, outF, options, type=None):
    "Transcodes a file"
    if type == None:
        type = os.path.splitext(outF)[1][1:].lower()
    #Get the file's metadata
    meta = decoders.getMetadata(inF)
    #Decode the file
    f = tempfile.NamedTemporaryFile()
    inF_real = decoders.decode(inF, f.name)
    if not inF_real:
        return False

    #Encode it
    succ = encoders.encode(inF_real, outF, type, options, meta)
    #Clean up
    f.close()
    return succ
