#!/usr/bin/env python

from distutils.core import setup

setup(name='libpulseaudio',
      version='0.9.22.1',
      description='simple libpulseaudio bindings',
      author='Valodim',
      author_email='valodim@mugenguild.com',
      license='LGPL',
      url='http://github.com/valodim/python-pulseaudio',
      packages=['pulseaudio'],
      provides=['libpulseaudio']
      download_url='http://datatomb.de/~valodim/libpulseaudio-0.9.22.1.tar.gz'
     )
