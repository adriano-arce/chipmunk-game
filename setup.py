###############################################################
# How to run this script from the command-line:               #
# 0. Add C:\Python34 to the PATH environment system variable. #
# 1. Navigate to this file's folder in Windows Explorer.      #
# 2. Enter "cmd" into the address bar.                        #
# 3. Copy-paste (by right-clicking): "python setup.py py2exe" #
###############################################################

import py2exe
from glob import glob
from distutils.core import setup


setup(console=['chipmunk_game.py'],
      data_files=[('imgs', glob('imgs/*.*'))],
      options={'py2exe': {'bundle_files': 1}},
      requires=['py2exe'],
      zipfile=None)

__all__ = ["py2exe"]