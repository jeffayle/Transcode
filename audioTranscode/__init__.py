#!/usr/bin/env python
# Copyright (c) 2010, Jeffrey Aylesworth <jeffrey@aylesworth.ca>
# 
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
import config
import sys
import os
import shlex
from glob import glob
from doTranscode import transcode, mtranscode

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

def main_multi():
    "Multiple mode for `transcodeall` command"
    if len(sys.argv) >= 2:
        config.quiet = True
        files = sys.argv[1:]
        jobs = [ ]
        copy = [ ]
        print "Welcome to transcodeall!"
        print "Add transcoding jobs in this format:"
        print "do <format> <directory> <encoder options>"
        print "do mp3 MP3-320 -b 320"
        print ""
        print "To copy files to each directory:"
        print "cp <files>"
        print "cp *.jpg CD.cue"
        print ""
        print "Directory will be created if it does not exist"
        print "Blank line will end input, start transcoding"
        while True:
            line = shlex.split(raw_input('> '))
            if line == []:
                break
            elif line[0] == 'do':
                if len(line) >= 3:
                    jobs.append(line[1:])
                else:
                    print "Not enough arguments for `do`"
            elif line[0] == 'cp':
                total = 0
                for f in line[1:]:
                    new = glob(f)
                    total += len(new)
                    copy += new
                print "Adding %d files to copy."%total
            else:
                print "Unknown command `%s`"%line[0]
        mtranscode(sys.argv[1:], jobs, copy)
    else:
        print "Transcode: ImageMagick inspired audio transcoding"
        print "---"
        print "Usage: (interactive)"
        print "%s <files>"%(sys.argv[0])
