import socket

# Set up a socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)

# Wait for a client to connect
print("Waiting for client to connect...")
client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)

# Send a message to the client
message = "hello world"
print("Sending message:", message)
client_socket.sendall(message.encode())

# Clean up
client_socket.close()
server_socket.close()
