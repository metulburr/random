
#!/usr/bin/env python3
#get facebook login html

import urllib, http.cookiejar, re, os, sys, getpass
#http.cookiejar


class Facebook():
	def __init__(self, email, password):
		self.email = email
		self.password = password

		cj = http.cookiejar.CookieJar()
		opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
		opener.addheaders = [('Referer', 'http://login.facebook.com/login.php'),
							('Content-Type', 'application/x-www-form-urlencoded'),
							('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)')]
		self.opener = opener
		
	def send(self):
		pass
	def recv(self):
		pass

	def login(self):
		url = 'https://login.facebook.com/login.php?login_attempt=1'
		data = "locale=en_US&non_com_login=&email="+self.email+"&pass="+self.password+"&lsd=20TOl"

		data = data.encode('ascii')
		usock = self.opener.open('http://www.facebook.com')
		usock = self.opener.open(url, data)
		page = usock.read().decode()
		if "Logout" in page:
			print("Logged in.")
			print(page)
		else:
			print("failed login")
			print(usock.read())
			sys.exit()
			

email = input('Email:')
passwd = getpass.getpass('Password:')
f = Facebook(email, passwd)
f.login()
