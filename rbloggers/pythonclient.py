import socket

HEADER = 64

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 6011))
while 1:
	data = bytes(input("Enter text to be upper-cased, q to quit\n"), 'UTF-8')
	data += b' ' * (HEADER - len(data))
	client_socket.send(data)
	if (data == 'q' or data == 'Q'):
		client_socket.close()
		break
	else:        
		data = client_socket.recv(HEADER).strip()
		print("Your upper cased text:  " , data)