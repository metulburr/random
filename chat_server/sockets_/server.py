import socket
import threading

class Server:
	def __init__(self, host, port):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.prompt = '>'
		self.buff = 1024
		self.host = host
		self.port = port
		self.sock.bind((self.host,self.port))
		self.max_conn = 5
		self.sock.listen(self.max_conn)
			
	def recv(self):
		self.conn, self.addr = self.sock.accept()
		while True:
			data = self.conn.recv(self.buff)
			if data:
				print('{} {}'.format(self.addr, data))
				
	def send(self):
		while True:
			user = input(self.prompt)
			user = 'SERVER: ' + user
			self.conn.send(user.encode())
		
	def run(self):
		for i in range(self.max_conn):
			threading.Thread(target=self.recv).start()		
			threading.Thread(target=self.send).start()		
		#while True:
		#	self.send()
			
server = Server('', 8003)
server.run()
		


