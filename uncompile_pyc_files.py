#https://github.com/wibiti/uncompyle2
#sudo python setup.py install

import uncompyle2

filename = 'game'
with open('{}.py'.format(filename), "wb") as f:
    uncompyle2.uncompyle_file('{}.pyc'.format(filename), f)
