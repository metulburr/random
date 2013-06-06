#!/usr/bin/env python3

version = 0.1

import sys


changes = {

	#name changes
	'__builtin__':'builtins',
	'ConfigParser':'configparser',
	'copy_reg':'copyreg',
	'cPickle':'pickle',
	'Queue':'queue',
	'repr':'reprlib',
	'SocketServer':'socketserver',
	'Tkinter':'tkinter',
	'_winreg':'winreg',
	'thread':'_thread',
	'dummy_thread':'_dummy_thread',
	'markupbase':'_markupbase',
	
	#Reorganization
	'xrange()':'range()',
	'reduce()':'functools.reduce()',
	'intern()':'sys.intern()',
	'unichr()':'chr()',
	'basestring()':'str()',
	'long()':'int()',
	'itertools.izip()':'zip()',
	'itertools.imap()':'map()',
	'itertools.ifilter()':'filter()',
	'itertools.ifilterfalse()':'itertools.filterfalse()',
	'cookielib':'http.cookiejar',
	'Cookie':'http.cookies',
	'htmlentitydefs':'html.entities',
	'HTMLParser':'html.parser',
	'httplib':'http.client',
	'Dialog':'tkinter.dialog',
	'FileDialog':'tkinter.FileDialog',
	'ScrolledText':'tkinter.scolledtext',
	'SimpleDialog':'tkinter.simpledialog',
	'Tix':'tkinter.tix',
	'Tkconstants':'tkinter.constants',
	'Tkdnd':'tkinter.dnd',
	'tkColorChooser':'tkinter.colorchooser',
	'tkCommonDialog':'tkinter.commondialog',
	'tkFileDialog':'tkinter.filedialog',
	'tkFont':'tkinter.font',
	'tkMessageBox':'tkinter.messagebox',
	'tkSimpleDialog':'tkinter.simpledialog',
	'robotparser':'urllib.robotparser',
	'urlparse':'urllib.parse',
	'cStringIO.StringIO()':'io.StringIO',
	'UserString':'collections.UserString',
	'UserList':'collections.UserList',
	
	#merged modules
	'BaseHTTPServer':'http.server',
	'CGIHTTPServer':'http.server',
	'SimpleHTTPServer':'http.server',
	'whichdb':'dbm',
	'anydbm':'dbm',
	'dbm':'dbm.ndbm',
	'dumbdbm':'dbm.dumb',
	'gdbm':'dbm.gnu',
	'dbm':'dbm.ndbm',
	#'dbm':'dbm.ndbm',
	'DocXMLRPCServer':'xmlrpc.server',
	'SimpleXMLRPCServer':'xmlrpc.server',
	'commands':'subprocess',
	
	#moved
	#'reduce()':'functools.reduce()',
	'reload()':'imp.reload()',
	
	#urlib
	'urllib.urlopen()':' urllib.request.urlopen()',
	'urllib.urlretrieve()':'urllib.request.urlretrieve()',
	'urllib.urlcleanup()':'urllib.request.urlcleanup()',
	'urllib.quote()':'urllib.parse.quote()',
	'urllib.quote_plus()':'urllib.parse.quote_plus()',
	'urllib.unquote()':'urllib.parse.unquote()',
	'urllib.unquote_plus()':'urllib.parse.unquote_plus()',
	'urllib.urlencode()':'urllib.parse.urlencode()',
	'urllib.pathname2url()':'urllib.request.pathname2url()',
	'urllib.url2pathname()':'urllib.request.url2pathname()',
	'urllib.getproxies()':'urllib.request.getproxies()',
	'urllib.URLopener':'urllib.request.URLopener',
	'urllib.FancyURLopener':'urllib.request.FancyURLopener',
	'urllib.ContentTooShortError':'urllib.error.ContentTooShortError',
	
	#urllib2
	'urllib2.urlopen()':'urllib.request.urlopen()',
	'urllib2.install_opener()':'urllib.request.install_opener()',
	'urllib2.build_opener()':'urllib.request.build_opener()',
	'urllib2.URLError':'urllib.error.URLError',
	'urllib2.HTTPError':'urllib.error.HTTPError',
	'urllib2.Request':'urllib.request.Request',
	'urllib2.OpenerDirector':'urllib.request.OpenerDirector',
	'urllib2.BaseHandler':'urllib.request.BaseHandler',
	'urllib2.HTTPDefaultErrorHandler':'urllib.request.HTTPDefaultErrorHandler',
	'urllib2.HTTPRedirectHandler':'urllib.request.HTTPRedirectHandler',
	'urllib2.HTTPCookieProcessor':'urllib.request.HTTPCookieProcessor',
	'urllib2.ProxyHandler':'urllib.request.ProxyHandler',
	'urllib2.HTTPPasswordMgr':'urllib.request.HTTPPasswordMgr',
	'urllib2.HTTPPasswordMgrWithDefaultRealm':'urllib.request.HTTPPasswordMgrWithDefaultRealm',
	'urllib2.AbstractBasicAuthHandler':'urllib.request.AbstractBasicAuthHandler',
	'urllib2.HTTPBasicAuthHandler':'urllib.request.HTTPBasicAuthHandler',
	'urllib2.ProxyBasicAuthHandler':'urllib.request.ProxyBasicAuthHandler',
	'urllib2.AbstractDigestAuthHandler':'urllib.request.AbstractDigestAuthHandler',
	'urllib2.HTTPDigestAuthHandler':'urllib.request.HTTPDigestAuthHandler',
	'urllib2.ProxyDigestAuthHandler':'urllib.request.ProxyDigestAuthHandler',
	'urllib2.HTTPHandler':'urllib.request.HTTPHandler',
	'urllib2.HTTPSHandler':'urllib.request.HTTPSHandler',
	'urllib2.FileHandler':'urllib.request.FileHandler',
	'urllib2.FTPHandler':'urllib.request.FTPHandler',
	'urllib2.CacheFTPHandler':'urllib.request.CacheFTPHandler',
	'urllib2.UnknownHandler':'urllib.request.UnknownHandler',
	
	#replacements
	'reload(M)':'imp.reload(M) (or exec)',
	'apply(f, ps, ks)':'f(*ps, **ks)',
	"'X'":'repr(X)',
	'X <> Y':'x != Y',
	'D.has_key(K)':'K in D  (or D.get(key) != None)',
	'raw_input(K)':'input(K)',
	'old input':'eval(input())',
	'file':'open(and io module classes)',
	'X.next':'X.__next__,called by next(X)',
	'X.__getslice__':'X.__getitem__ passed a slice object',
	'X.__setslice__':'X.__setitem__ passed a slice object',
	'execfile(filename)':'exec(open(filename).read())',
	'exec open(filename)':'exec(open(filename).read())',
	'print x, y':'print(x, y)',
	'print >> F, x, y':'print(x, y, file=F)',
	'print x, y,':"print(x, y, end=' ')",
	"u'ccc'":"'ccc'",
	"'bbb' for byte in strings":"b'bbb'",
	'except E, V:':'except E as X:',
	'def f((a, b)):':'def f(x): (a, b) = x',
	'file.xreadlines':'for line in file: (or X=iter(file))',
	'D.keys, etc. as lists':'list(D.keys()) (dictionary views)',
	'map(), range, etc. as lists':'list(map()), list(range()) (built-ins)',
	'map(None, ...)	':'zip(or manuel code to pad results)',
	'X=D.keys(); X.sort()':'sorted(D) (or list(D.keys()))',
	'cmp(x, y)':'(x > y) - (x < y)',
	'X.__cmp__(y)':'__lt__, __gt__, __eq__, etc.',
	'X.__nonzero__':'X.__bool__',
	'X.__hex__, X.__oct__':'X.__index__',
	'sort comparison functions':'Use key=transform or reverse=True',
	'Dictionary <, >, <=, >=	':'compare sorted(D.items()) (or loop code)',
	'types.ListType':'list(types is for nonbuilt-in names only)',
	'__metaclass__ = M':'class C(metaclass=M):',
	'sys.exc_type, exc_value':'sys.exc_info()[0], [1]',
	'function.func_code':'function.__code__',
	'__getattr__ run by built-ins':'Redefine __X__ methods in wrapper classes',
	'-t, -tt command-line switches':'inconsistant tabs/spaces use is always an error',
	'from ... *, within a function':'May only appear at the top level of a file',
	'import mod, in same package':'from . import mod, package=relative form',
	'class MyException ':'class MyException(Exception)',
	'exceptions module':'built-in scope, library manual',
	'os.popen2, os.popen3, os.popen4':'subprocess.Popen()',
	'String-based exceptions':'Class-based exceptions (also required in 2.6)',
	'String module functions':'String object methods',
	'Unbound methods':'Functions (staticmethod to call via instance)',
	'Mixed type comparisons, sorts':'Nonnumeric mixted type comparisons are errors',
	
	#others
	'raise TypeError, msg, tb':'raise TypeError.with_traceback(tb)',
	'raise "ahhhh!"':'raise Exception("ahhhh!")',
	'gen.throw(ValueError, "bad value")':'gen.throw(ValueError("bad value"))',
	'type(obj) == types.DictType':'isinstance(obj, dict)',
	
	#division
	'1/10 = 0':'1/10 = 0.1',
	'1.0/10 = 0.10000000000000001':'1.0/10 = 0.1',
	'10/1 = 10':'10/1 = 10.0',
	}
	
def search(d, viewall=None):
	def printer(k,v):
		print('-' * 25)
		print('Python 2x: {}'.format(k))
		print('Python 3x: {}'.format(v))
		print('-' * 25)
	
	if len(sys.argv) == 1:
		print('Enter 2.x or 3.x to view changes, ENTER to view all')
		searchfor = input('SEARCH: ')
	elif len(sys.argv) == 2:
		if sys.argv[1] == '-viewall':
			viewall = 'viewall'
		searchfor = sys.argv[1]

	for key, val in d.items():
		if searchfor == key or searchfor == val:
			printer(key,val)
		elif searchfor in key or searchfor in val:
			printer(key,val)
		elif viewall:
			printer(key,val)
			

search(changes)




