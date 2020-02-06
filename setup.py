#!/usr/bin/env python
from setuptools import setup

with open('README.md', 'r') as file:
    long_description = file.read()

with open('requirements.txt') as file:
    install_requires = [line.rstrip('\r\n') for line in file]

setup(
  name = 'dmiapi',
  packages = ['dmiapi'],
  version = '0.1.2',
  license = 'MIT',
  description = 'Wrapper for access weather observations and forecasts from the Danish Metrology Institute (DMI) API',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Niklas Christoffer Petersen',
  author_email = 'nikalscp@gmail.com',
  url = 'https://github.com/niklascp/py-dmiapi',
  download_url = 'https://github.com/niklascp/py-dmiapi/archive/v0.1.0.tar.gz',
  keywords = ['weather', 'metrology', 'forecast', 'dmi'],
  install_requires = install_requires,
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License'
  ],
)
