import socket  
import threading

class Client:
	def __init__(self, host, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.prompt = '>'
		self.buff = 1024
		self.host = host
		self.port = port
		self.sock.connect((self.host, self.port))

	def recv(self):
		while True:
			data = self.sock.recv(self.buff)
			if data:
				print(data)
				
	def send(self):
		user = input(self.prompt)
		user = 'CLIENT: ' + user
		self.sock.send(user.encode())
		
	def run(self):
		threading.Thread(target=self.recv).start()
		while True:
			self.send()


client = Client(socket.gethostname(), 8003)
client.run()
