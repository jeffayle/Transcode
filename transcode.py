#!/usr/bin/env python
import config
import sys
from doTranscode import transcode

if len(sys.argv) >= 3:
    inF = sys.argv[1]
    outF = sys.argv[-1]
    options = sys.argv[2:-1]
    
    succ = transcode(inF, outF, options)
    if not succ:
        sys.stderr.write("Something bad happened :(")
        sys.stderr.write("Check encoder options\n")

else:
    print "Transcode: ImageMagick inspired audio transcoding"
    print "---"
    print "Usage:"
    print "%s <input> [options] <output>"%(sys.argv[0])
