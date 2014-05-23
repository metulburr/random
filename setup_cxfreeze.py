import sys
from cx_Freeze import setup, Executable
import os
import shutil
import time

RESOURCES_DIR = 'resources'

build_exe_options = {"packages": ["os"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
    'pywin.debugger.dbgcon', 'pywin.dialogs']
packages = []
path = []


GUI2Exe_Target_1 = Executable(
    script = "game.py",
    initScript = None,
    base = base,
    #targetDir = r"dist",
    targetName = "game.exe",
    compress = True,
    copyDependentFiles = True,
    appendScriptToExe = True,
    appendScriptToLibrary = True,
    icon = None
)

setup(
    version = "0.1",
    description = "No Description",
    author = "No Author",
    name = "cx_Freeze Sample File",
    options = {
        "build_exe": {
            "includes": includes,
            "excludes": excludes,
            "packages": packages,
            "path": path
            }
        },
    executables = [GUI2Exe_Target_1]
)

path = ''
directory = os.listdir('build')
for d in directory:
    if d.startswith('exe.win'):
        path = 'build/{}'.format(d)

shutil.copytree(RESOURCES_DIR, '{}/{}'.format(path, RESOURCES_DIR))
#shutil.rmtree('build')
name = time.strftime("%Y%m%d-%H%M%S", time.localtime())
os.rename('build', 'exe build {}'.format(name))

