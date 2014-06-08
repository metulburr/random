import ctypes
import os

#linux requires fullpath, not CWD
path = os.path.dirname(os.path.abspath(__file__))
fullpath = os.path.join(path, 'testlib.so')

ctypes.cdll.LoadLibrary(fullpath)
testlib = ctypes.CDLL(fullpath)
testlib.myprint()


#windows searches CWD
#testlib = cdll.LoadLibrary('testlib.dll')
