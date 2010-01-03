#!/usr/bin/env python
import config
import sys

config.createState()

#Check arguments
if len(sys.argv) >= 2:
    command = sys.argv[1]
else:
    command = None
