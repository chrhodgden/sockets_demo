#https://youtu.be/3QiPPX-KeSc

import socket
import threading

HEADER = 64
PORT = 6011
SERVER = 'localhost'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISSCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	print(f"[NEW CONNECRION] {addr} connected")
	connected = True
	while connected:
		msg = conn.recv(HEADER).decode(FORMAT).strip()
		if msg == DISCONNECT_MESSAGE:
			connected = False
		print(f"[{addr}] {msg}")
		msg = bytes(msg.upper(), FORMAT)
		msg += b' ' * (HEADER - len(msg))
		conn.send(msg)
	
	conn.close()
	    
def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()