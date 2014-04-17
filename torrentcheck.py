#donwload latest ubuntu
#python2.x or python3.x
#pass -h argument for help

#example command; download ubuntu 14.04 32 bit with transmission:
#   python SCRIPTNAME.py -r 14.04 -c transmission-gtk -i 


try:
    from urllib2 import Request, urlopen
    from urllib2 import HTTPError
except ImportError:
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
import subprocess
import os
import argparse
import time
import sys

parser = argparse.ArgumentParser(description='Download Ubuntu')
parser.add_argument('-a','--amd64', action='store_true',
    help='Download 64 bit Ubuntu')
parser.add_argument('-i','--i386', action='store_true',
    help='Download 32 bit Ubuntu')
parser.add_argument('-r' , '--release', default='14.04',
    help='Ubuntu release number, RELEASE default is 14.04')
parser.add_argument('-f' , '--freq', default=1, type=int,
    help='Check for torrent file every X minutes, FREQ default is 1')
parser.add_argument('-t' , '--timeout', default=25, type=int,
    help='change socket timeout, TIMEOUT default is 1')
parser.add_argument('-c' , '--client', default='rtorrent',
    help='change torrent client used to download, CLIENT default is rtorrent')
args = vars(parser.parse_args())



release = args['release']
TORRENT_URL_i386 = r'http://releases.ubuntu.com/{0}/ubuntu-{0}-desktop-i386.iso.torrent'.format(release)
TORRENT_URL_AMD64 = r'http://releases.ubuntu.com/{0}/ubuntu-{0}-desktop-amd64.iso.torrent'.format(release)
if args['i386']:
    link = TORRENT_URL_i386
else:
    link = TORRENT_URL_AMD64
freq = args['freq']
timeout = args['timeout']
torrent_client = args['client']
TORRENT_FILE_PATH = os.path.abspath('ubuntu_{}.torrent'.format(release))
    
req = Request(link)
while True:
    try:
        try:
            torrent_url = urlopen(req, timeout=timeout)
        except:
            time.sleep(freq*60)
            continue
        torrent_contents = torrent_url.read()
        torrent_file = open(TORRENT_FILE_PATH, "wb")
        torrent_file.write(torrent_contents)
        torrent_file.close()
        cmd = '{} {}'.format(torrent_client, TORRENT_FILE_PATH)
        subprocess.Popen(cmd.split())
        break
    except KeyboardInterrupt:
        print()
        sys.exit()
print('Download complete')
