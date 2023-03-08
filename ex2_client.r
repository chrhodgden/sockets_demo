input <- function(prompt = "") {
	fil <- file("stdin")
	open(fil)
	cat(prompt)
	inp <- readLines(fil, n = 1)
	return(inp)
}

sock_client <- make.socket(host = "localhost", 6011, server = FALSE)

data <- input("demo input: ")
data <- c(1, 0, 0, 1)
data <- as.character(data)
cat(data, "\n")
# data <- charToRaw(data)
# data <- rawToBits(data)
write.socket(sock_client, data)
data <- read.socket(sock_client)
cat(data, "\n")
close.socket(sock_client)
