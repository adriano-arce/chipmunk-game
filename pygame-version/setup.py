# How to run this script from the command-line:
# 1. Navigate to this file's folder in Windows Explorer.
# 2. Enter "cmd" into the address bar.
# 3. Copy-paste (by right-clicking): "python setup.py py2exe"

from glob import glob
from distutils.core import setup
import py2exe

data_files = [('images', glob('images/*.*'))]
setup(console=['chipmunk-game.py'], data_files = data_files)