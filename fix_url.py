try:
    import urlparse as parser
except ImportError:
    import urllib.parse as parser

def fix_url(website):
    http = 'http://'
    www = 'www.'
    end='.com'
    new_url = ''
    
    if not website.startswith(http):
        if website.startswith(www):
            new_url += http + website
        else:
            new_url += http + www + website
    else:
        new_url = website
    if not website.endswith(end):
        new_url += end
    return new_url
    
variations = [
    'metulburr',
    'www.metulburr',
    'http://www.metulburr.com',
    'http://www.metulburr',
    'www.metulburr.com',
    'metulburr.com',
]

for variation in variations:
    print(fix_url(variation))
