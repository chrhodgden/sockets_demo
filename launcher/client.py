import socket

HEADER = 64
PORT = 6011
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DIS'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

connected = True

while connected:
	data = input("Enter text to be upper-cased, q to quit\n")

	if (data.lower() == 'q' or data == DISCONNECT_MESSAGE):
		data = DISCONNECT_MESSAGE
		connected = False

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

	client_socket.send(data)

	data = client_socket.recv(HEADER)
	if data == b'\x00':
		print("ALERT")
		data = client_socket.recv(HEADER)

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

client_socket.close()