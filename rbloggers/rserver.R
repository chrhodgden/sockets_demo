HEADER <- 64
PORT <- 6011
SERVER <- "localhost"
FORMAT <- "utf-8"
DISCONNECT_MESSAGE <- "!DISSCONNECT"

cat("Listening...\n")

con <- socketConnection(
	host = "localhost",
	port = 6011,
	server = TRUE
)

connected <- TRUE

while (connected) {
	data <- trimws(readChar(con, HEADER))
	while (length(data) == 0) {
		cat("ALERT\n")
		data <- trimws(readChar(con, HEADER))
	}
	if (data == DISCONNECT_MESSAGE) connected <- FALSE
	cat(data, "\n")
	data <- toupper(data)
	data <- paste(data, strrep(" ", HEADER - nchar(data)), sep = "")
	writeChar(data, con)
}

close(con)