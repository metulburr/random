

import sys
from urllib.request import urlopen
import os




class Downloader:
	def __init__(self, url, destpath=''):

		if url[:4] != 'http':
			return 
		
		file_name = os.path.basename(url) 
		u = urlopen(url)
		f = open(os.path.join(destpath,file_name), 'wb')
		try:
			file_size = int(u.info()["Content-Length"])
		except TypeError:
			file_size = len(u.read())

		file_size_dl = 0
		block_sz = 8192
		while True:
			buffer = u.read(block_sz)
			if not buffer: #end of file
				print()
				break
			file_size_dl += len(buffer)
			f.write(buffer)
			
			progress = float(file_size_dl) / file_size
			status = r"Downloading: {0} {1}/{2}  [{3:.2%}]".format(file_name,file_size_dl, file_size, progress)
			status = status + chr(8)*(len(status)+1)
			sys.stdout.write(status)

		f.close()

if __name__ == '__main__':
	#url = 'http://www.metulburr.com/video/megadeth.mp4'
	#Downloader(url)
	Downloader('https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft.jar')
	Downloader('https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar')
	Downloader('https://s3.amazonaws.com/MinecraftDownload/launcher/Minecraft_Server.exe')
	Downloader('ftp://193.43.36.131/Radio/MP3/2011/Accra-Ada-Ndeso-Atanga-en.mp3')
