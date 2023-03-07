HEADER <- 64
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
	server = FALSE
)

connected <- TRUE

while (connected) {
	sendme <- input("input text (q to quit): ")
	if (sendme == "q" | sendme == DISCONNECT_MESSAGE) {
		sendme <- DISCONNECT_MESSAGE
		connected <- FALSE
	}
	sendme <- paste(sendme, strrep(" ", HEADER - nchar(sendme)), sep = "")
	writeBin(sendme, con)
	server_resp <- trimws(readBin(con, "character", HEADER))
	if (length(server_resp) == 0) {
		cat("ALERT\n")
		server_resp <- trimws(readBin(con, "character", HEADER))
	}
	cat(paste("Your upper cased text: ", server_resp, "\n"))
}

close(con)