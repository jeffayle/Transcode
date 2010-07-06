#!/usr/bin/env python
import encoders
import decoders
import config
import tempfile
import os
import errno
import shutil

def transcode(inF, outF, options, type=None):
    "Transcodes a file"
    if type == None:
        type = os.path.splitext(outF)[1][1:].lower()
    #Get the file's metadata
    meta = decoders.getMetadata(inF)
    #Decode the file
    f = tempfile.NamedTemporaryFile(suffix=".wav")
    inF_real = decoders.decode(inF, f.name)
    if not inF_real:
        return False

    #Encode it
    succ = encoders.encode(inF_real, outF, type, options, meta)
    #Clean up
    f.close()
    return succ

def mtranscode(files, jobs, copy):
    "Multiple file transcoding processor"
    print "- Creating directories for transcoding"
    #Create all the directories
    for job in jobs:
        try:
            os.makedirs(job[1])
        except OSError as exc:
            if exc.errno == errno.EEXIST:
                pass
            else: raise
    #Copy static files
    print "- Copying static files"
    for f in copy:
        for job in jobs:
            shutil.copy(f, job[1])
