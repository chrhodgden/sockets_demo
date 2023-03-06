import socket

HEADER = 64
PORT = 6011
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = b'!DISSCONNECT'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

connected = True

while connected:
	data = input("Enter text to be upper-cased, q to quit\n")
	if (data.lower() == 'q' or data == DISCONNECT_MESSAGE):
		data = DISCONNECT_MESSAGE.decode(FORMAT)
		connected = False
	data = bytes(data, FORMAT)
	data += b' ' * (HEADER - len(data))
	client_socket.send(data)
	data = client_socket.recv(HEADER).strip()
	if data == b'\x00':
		print("ALERT")
		data = client_socket.recv(HEADER).strip()
	data = data.decode(FORMAT)
	print("Your upper cased text: " , data)

client_socket.close()