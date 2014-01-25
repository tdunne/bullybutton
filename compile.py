# VERY simple script to compile the python script to an exe using py2exe
from distutils.core import setup
import py2exe

setup(console=['bullybutton.py'])
