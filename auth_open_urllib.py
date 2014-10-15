try:
    import urllib2 as REQ
    import urlparse as PAR
except ImportError:
    import urllib.request as REQ
    import urllib.parse as PAR
 
rooturl='http://www.routerlogin.net' # admin url of the router
username = 'admin'
password = 'password'

# create a urllib opener for basic authentication
passman = REQ.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, rooturl, username, password)
authhandler = REQ.HTTPBasicAuthHandler(passman)
opener = REQ.build_opener(authhandler)
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
REQ.install_opener(opener)

req = REQ.urlopen(rooturl + '/adv_index.htm')
html = req.read().decode()
print(html)
