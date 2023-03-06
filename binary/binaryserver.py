import socket
import threading

HEADER = 64
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
		data = conn.recv(HEADER).strip()
		if data == b'\x00':
			print("ALERT")
			data = conn.recv(HEADER).strip()
		if data == DISCONNECT_MESSAGE:
			connected = False
		print(f"[{addr}] <{data}>")
		data = data.upper()
		data += b' ' * (HEADER - len(data))
		conn.send(data)
	
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