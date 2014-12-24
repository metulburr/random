
#easy_install bbfreeze

from bbfreeze import Freezer

f = Freezer("dist")
f.addScript('pyroller/pyroller.py')
f()

#python setup.py
#creates a dsit directory wtih libs, using root fil pyroller/pyroller.py
