#!/usr/bin/env python
from distutils.core import setup

setup(
    name = 'AudioTranscode',
    version = '1.0',
    packages = ['audioTranscode','audioTranscode.encoders','audioTranscode.decoders'],
    scripts = ['transcode'],
    author = 'Jeffrey Aylesworth',
    author_email = 'jeffrey@aylesworth.ca',
    license = 'MIT',
    url = 'http://github.com/jeffayle/Transcode'
)
