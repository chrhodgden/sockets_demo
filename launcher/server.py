#What would I like to do?
# I would like to have the python script open a socket connection, as a server i guess, 
# then it would launch an R process that would connect to the socket
# The python procedure could then send a binary vector or 2 to the R procedure
# The R procedure would then either:
	# put binary vector foward prop through a neural network
		# and then send to python the output binary vector
	# or use the 2 binary vectors to train the the neural network
		# and then send to python the cost value
# I should consider a 3rd mode where we send the target output vector and the ANN trains from the previous fw prop

# So:
# python script runs,
# Python opens socket as server
# python runs R script
# R procedure connects to socket as client
# Python procedure sends R procedure a binary vector
# R procedure modifies the binary vector
# R procedure sends Python procedure a binary vector
# Process loops until we need to stop, probably from user
# Python procedure sends R a disconnect signal
# R procedure closes socket
# R procedure ends
# Python procedure ends 

import socket
import struct
import threading

HEADER = 64
PORT = 6011
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'SID!'
DISCONNECT_SIGNAL = b'\x01\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x01\x00\x00\x01\x00\x01\x00\x01\x00\x00\x01\x01'

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

		if data == DISCONNECT_MESSAGE or data == "".join(reversed(DISCONNECT_MESSAGE)):
			connected = False

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
		data = data.replace('b', '')
		print(data, type(data))
		data = ''.join(reversed(data))
		print(data, type(data))

		n = b''
		for b in data:
			m = int(b)
			m = chr(m)
			m = bytes(m, 'utf-8')
			n += m

		data = n
		print(data, type(data))

		conn.send(data)

	conn.close()
	    
def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	conn, addr = server.accept()
	handle_client(conn, addr)

print("[STARTING] server is starting...")
start()