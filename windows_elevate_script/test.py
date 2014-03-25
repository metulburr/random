import ctypes
import subprocess
import sys
import os

if os.name == 'nt':
    if ctypes.windll.shell32.IsUserAnAdmin():
        print('You are admin')
    else:
        print('You are not admin')

input('Press Enter')
