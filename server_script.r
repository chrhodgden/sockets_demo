# Set up a socket client
sock <- socketConnection(host = "localhost", port = 9999, server = TRUE)
open(sock, "w")

# Send a message to the server
message <- "Hello world! This message is from the R server."
cat("Sending message:", message, "\n")
writeLines(message, sock)

# Clean up
close(sock)