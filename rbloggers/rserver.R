HEADER <- 64

server <- function(){
  while(TRUE){
    writeLines("Listening...")
    con <- socketConnection(
		host="localhost",
		port = 6011,
		blocking=TRUE,
		server=TRUE,
		open="r+"
)
	data <- trimws(readChar(con, HEADER))
    print(data)
    response <- toupper(data)
	writeChar(response, con)
    close(con)
  }
}
server()