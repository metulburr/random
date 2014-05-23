
#intended for Pygame/python2.x
#where game structure is:
#game.py (starting script)
#   /resources (subdirectories of required font, images, sound, music, etc.)
#   /data (all source files)
#copies required resources directory to exe location
#names exe directory as build time

#python setup.py py2exe

import os
import sys
import py2exe
from distutils.core import setup
import shutil
import time

START_SCRIPT = 'game.py'
RESOUCES_DIR = 'resources'

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    dlls = ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll")
    if os.path.basename(pathname).lower() in dlls:
        return 0
    return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

sys.argv.append('py2exe')
setup(
    options={
        'py2exe': {
            'bundle_files': 1, #bundle dlls into exe
            'compressed': True,
            'dll_excludes': ['w9xpopen.exe'], #do not inlcude w9xpopen.exe 
        }
    },
    windows=[{'script': START_SCRIPT}],
    zipfile=None, #bundle libraries into exe
)

shutil.copytree(RESOUCES_DIR, 'dist/{}'.format(RESOUCES_DIR))
shutil.rmtree('build')
name = time.strftime("%Y%m%d-%H%M%S", time.localtime())
os.rename('dist', 'exe build {}'.format(name))

