import socket
import struct
import threading

HEADER = 32
PORT = 6011
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = b'!DISSCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	print(f"[NEW CONNECRION] {addr} connected")
	connected = True
	while connected:

		data = conn.recv(HEADER)
		if data == b'\x00':
			print("ALERT")
			data = conn.recv(HEADER)
		
		print(f"[{addr}] <{data}>")
		print(data, type(data))
		n = ""
		for b in data: n = f'{b}{n}'
		data = n
		print(data, type(data))
		data = int(data, 2)
		print(data, type(data))
		data = hex(data)
		print(data, type(data))
		data = data.lstrip('0x')
		print(data, type(data))
		data = bytearray.fromhex(data)	
		print(data, type(data))
		data = data.decode()
		print(data, type(data))
		data = data.upper()
		print(data, type(data))
		
		n = ""
		for s in data: n += hex(ord(s)).lstrip('0x')
		data = n
		print(data, type(data))

		data = int(data, 16)
		print(data, type(data))

		data = bin(data)
		print(data, type(data))

		data = data.lstrip('0b')
		print(data, type(data))

		n = b''
		for s in data: 
			m = int(s)
			m = bytes(m)
			print(m, type(m))
			n += m
		
		data = n
		print(data, type(data))

#		conn.send(data)

		connected = False
	
	conn.close()
	    
def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	conn, addr = server.accept()
	handle_client(conn, addr)

print("[STARTING] server is starting...")
start()