# Set up a socket client
con_client <- socketConnection(host = "localhost", port = 9999)
# open(con_client, "r")

# Receive a message from the server
message <- readLines(con_client)
print(message)
while(isIncomplete(con_client)) {
	message <- readLines(con_client)
	print(message)
}
cat("R Client:", message, "\n")

# Clean up
close(con_client)
