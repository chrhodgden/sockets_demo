# Set up a socket client
client <- socketConnection(host = "localhost", port = 9999)
open(client, "r")

# Receive a message from the server
message <- readLines(client, n = 1)
cat("Received message:", message, "\n")

# Clean up
close(client)