HEADER <- 32
PORT <- 6011
SERVER <- "localhost"
FORMAT <- "utf-8"
DISCONNECT_MESSAGE <- "!DISSCONNECT"

input <- function(prompt = "") {
	fil <- file("stdin")
	open(fil)
	cat(prompt)
	inp <- readLines(fil, n = 1)
	return(inp)
}

con <- socketConnection(
	host = SERVER,
	port = PORT,
	server = FALSE,
	open = "a+b"
)

connected <- TRUE

while (connected) {
	data <- input("input text (q to quit): ")
	if (data == "q" | data == DISCONNECT_MESSAGE) {
		data <- DISCONNECT_MESSAGE
		connected <- FALSE
	}

	data_len <- nchar(data)
	data_len <- as.raw(data_len)
	data_len <- rawToBits(data_len)
	writeBin(data_len, con)

	data <- paste(data, strrep(" ", HEADER - nchar(data)), sep = "")
	data <- charToRaw(data)
	data <- rawToBits(data)
	writeBin(data, con)
	server_resp <- trimws(readBin(con, "character", HEADER))
	if (length(server_resp) == 0) {
		cat("ALERT\n")
		server_resp <- trimws(readBin(con, "character", HEADER))
	}
	cat(paste("Your upper cased text: ", server_resp, "\n"))
}

close(con)