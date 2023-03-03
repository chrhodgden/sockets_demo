import socket

# Set up a socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

# Receive a message from the server
message = client_socket.recv(1024).decode()
print("Python Client:", message)

# Clean up
client_socket.close()