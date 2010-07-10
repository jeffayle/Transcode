#!/usr/bin/env python
from distutils.core import setup

setup(
    name = 'AudioTranscode',
    version = '2.0',
    packages = ['audioTranscode','audioTranscode.encoders','audioTranscode.decoders'],
    scripts = ['transcode', 'transcodeall'],
    author = 'Jeffrey Aylesworth',
    author_email = 'jeffrey@aylesworth.ca',
    license = 'MIT',
    url = 'http://github.com/jeffayle/Transcode'
)
