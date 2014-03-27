
import ctypes
import subprocess
import sys
import os

if os.name == 'nt':
	if not ctypes.windll.shell32.IsUserAnAdmin():
		print('\nThis script requires to be ran with admin privileges\n')
		sys.exit()

if sys.version[0] == '2':
	input = raw_input
	import _winreg as wreg
else:
	import winreg as wreg

#create key
key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\TestCompany\\TestProject")
# Create new subkey
wreg.SetValue(key, 'NewSubkey', wreg.REG_SZ, 'testsubkey')
print(wreg.QueryValue(key, 'NewSubKey'))
# prints 'testsubkey'
# Create new value
wreg.SetValueEx(key, 'ValueName', 0, wreg.REG_SZ, 'testvalue')
print(wreg.QueryValueEx(key,'ValueName'))
# prints (u'testvalue', 1)
key.Close()


#read value
key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "Software\\TestCompany\\TestProject",0,wreg.KEY_ALL_ACCESS)
wreg.SetValue(key, 'NewSubkey', wreg.REG_SZ, 'subkey_changed')
print(wreg.QueryValue(key, 'NewSubkey'))
# prints 'subkey_changed'
wreg.SetValueEx(key, 'ValueName', 0, wreg.REG_SZ, 'value_changed')
print(wreg.QueryValueEx(key, 'ValueName'))
key.Close()


#loop keys
keyVal = r"Software"
aKey = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, keyVal, 0, wreg.KEY_ALL_ACCESS)
try:
    i = 0;
    while True:
        asubkey = wreg.EnumKey(aKey, i)
        print(asubkey)
        i += 1
except WindowsError:
    pass

input('Press Enter')

