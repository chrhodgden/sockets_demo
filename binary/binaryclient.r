HEADER <- 64
PORT <- 6011
SERVER <- "localhost"
FORMAT <- "utf-8"
DISCONNECT_MESSAGE <- "!DIS"

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

	data <- input("input text: ")
	if (data == "q") {
		connected <- FALSE
		data <- DISCONNECT_MESSAGE
	}
	cat("{", data, "}", typeof(data), "\n")
	data <- charToRaw(data)
	cat("{", data, "}", typeof(data), "\n")
	data <- rawToBits(data)
	cat("{", data, "}", typeof(data), "\n")

	writeBin(data, con)

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

}

close(con)