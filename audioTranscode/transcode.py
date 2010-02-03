#!/usr/bin/env python
import config
import sys
import os
from doTranscode import transcode

if 'QUIET_TRANSCODE' in os.environ and os.environ['QUIET_TRANSCODE']!='0':
    config.quiet = True

def main():
    if len(sys.argv) >= 3:
        inF = sys.argv[1]
        outF = sys.argv[-1]
        options = sys.argv[2:-1]
    
        #If the output is just an extension (first character is a dot) use the
        #same name as the input file, with new extension
        if outF[0] == '.':
            outF = os.path.splitext(inF)[0] + outF
        
        succ = transcode(inF, outF, options)
        if not succ:
            sys.stderr.write("Something bad happened :(\n")
            sys.stderr.write("Check encoder options\n")
    
    else:
        print "Transcode: ImageMagick inspired audio transcoding"
        print "---"
        print "Usage:"
        print "%s <input> [options] <output>"%(sys.argv[0])
