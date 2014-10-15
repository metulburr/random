from urllib.parse import urlencode
from urllib.request import urlopen
import json as m_json

def google(string=None):
	query = input('Query: ')
	query = urlencode({'q':query})
	response = urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query).read()
	json = m_json.loads(bytes.decode(response))
	results = json['responseData']['results']
	for result in results:
		title = result['title']
		url = result['url']   # was URL in the original and that threw a name error exception
		print(url)
		
while True:
	google()
	print()