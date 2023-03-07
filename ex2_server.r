sock_server <- make.socket(
	host = "localhost",
	6011,
	server = TRUE
	)

connected <- TRUE
data <- read.socket(sock_server)
cat(data, "\n")
data <- toupper(data)
write.socket(sock_server, data)
close.socket(sock_server)
