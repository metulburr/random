
#easy_install bbfreeze

from bbfreeze import Freezer

f = Freezer("dist")
f.addScript('pyroller/pyroller.py')
f()

#python setup.py
#creates a dsit directory wtih libs, using root fil pyroller/pyroller.py

#matplotlib.numerix import error fix
#in file /usr/local/lib/python2.7/dist-packages/bbfreeze-1.1.3-py2.7.egg/bbfreeze/recipes
#wrap this lline mf.import_hook("matplotlib.numerix.random_array", m)
#in an try/except ImportError 
