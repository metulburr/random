import urllib
import urllib2
import sys
 
'''
send argv[1] file to codepad for quick show help
'''
 
url = 'http://codepad.org'
content=open(sys.argv[1]).read()
values = {'lang' : 'Python',
          'code' : content,
          'submit':'Submit'}
 
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
for href in the_page.split("</a>"):
    if "Link:" in href:
        ind=href.index('Link:')
        found = href[ind+5:]
        for i in found.split('">'):
            if '<a href=' in i:
                 print "The link: " ,i.replace('<a href="',"").strip()
