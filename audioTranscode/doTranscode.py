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
    #Do the transcoding
    print "- Starting decoding"
    for f in files:
        print "- Decoding %s"%f
        wav = tempfile.NamedTemporaryFile(suffix=".wav")
        wavName = decoders.decode(f, wav.name)
        meta = decoders.getMetadata(f)
        if not wavName:
            print " `- Decoding failed"
            continue
        else:
            print " `- Decoded"
        #Encode
        for job in jobs:
            type = job[0]
            dir = job[1]
            opts = job[2:]
            print " `- Encoding (%s %s)"%(type, " ".join(opts))
            outf= os.path.join(dir,
                (os.path.splitext(os.path.split(f)[1])[0] + '.' + type))
            stat = encoders.encode(wavName, outf, type, opts, meta)
            if stat:
                print "  `- Encoding successful"
            else:
                print "  `- Encoding failed"
