# Set up a socket client
sock <- socketConnection(host = "localhost", port = 9999)
open(sock, "w")

# Send a message to the server
message <- "hello world"
cat("Sending message:", message, "\n")
writeLines(message, sock)

# Clean up
close(sock)