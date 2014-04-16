#!/usr/bin/env python

import glib
import urllib2
import os.path
import subprocess

RELEASE_NO = "14.04"
#TORRENT_URL_i386 = "http://releases.ubuntu.com/%s/" \
#              "ubuntu-%s-desktop-i386.iso.torrent" % (RELEASE_NO, RELEASE_NO)
TORRENT_URL_AMD64 = "http://releases.ubuntu.com/%s/" \
              "ubuntu-%s-desktop-amd64.iso.torrent" % (RELEASE_NO, RELEASE_NO)
FREQ = 60 # frequency in minutes. Check for torrent file every x minutes
SOCKET_TIMEOUT = 25
TORRENT_FILE_PATH = os.path.abspath("ubuntu_12.04.torrent")


#req = urllib2.Request(TORRENT_URL_i386) # for i386 torrent
req = urllib2.Request(TORRENT_URL_AMD64) # for amd64 torrent

def check_cb():
	try:
		# check if file exists
		torrent_url = urllib2.urlopen(req, timeout=SOCKET_TIMEOUT)
	except urllib2.URLError:
		# file does not exist yet, keep checking for it
		return True
	else:
		global loop
		# 12.04 torrent file exists
		# get file and save it locally
		torrent_contents = torrent_url.read()
		torrent_file = open(TORRENT_FILE_PATH, "w")
		torrent_file.write(torrent_contents)
		torrent_file.close()
		# add file to transmission
		subprocess.Popen(["transmission-gtk", TORRENT_FILE_PATH])
		loop.quit()

glib.timeout_add_seconds(FREQ*60, check_cb)

loop = glib.MainLoop()
loop.run()
