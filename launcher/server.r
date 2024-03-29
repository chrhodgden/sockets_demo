HEADER <- 64
PORT <- 6011
SERVER <- "localhost"
FORMAT <- "utf-8"
DISCONNECT_MESSAGE <- "!DIS"

cat("Listening...\n")

con <- socketConnection(
	host = "localhost",
	port = 6011,
	server = TRUE,
	open = "a+b"
)

connected <- TRUE

while (connected) {
	data <- readBin(con, "raw", HEADER)
	while (length(data) == 0) {
		#cat("ALERT\n")
		data <- readBin(con, "raw", HEADER)
	}
	cat("{", data, "}", typeof(data), "\n")
	data <- packBits(data, "raw")
	cat("{", data, "}", typeof(data), "\n")
	data <- rawToChar(data)
	cat("{", data, "}", typeof(data), "\n")

	if (data == DISCONNECT_MESSAGE | data == paste(rev(DISCONNECT_MESSAGE), collapse = "")) {
		connected <- FALSE
	}

	data <- toupper(data)
	cat("{", data, "}", typeof(data), "\n")
	data <- charToRaw(data)
	cat("{", data, "}", typeof(data), "\n")
	data <- rawToBits(data)
	cat("{", data, "}", typeof(data), "\n")

	writeBin(data, con)

}

close(con)