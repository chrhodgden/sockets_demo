HEADER <- 64

client <- function(){
    con <- socketConnection(
		host="localhost",
		port = 6011,
		blocking=TRUE,
		server=FALSE,
		open="r+"
	)
    sendme <- "idhvoeovgo"
    if(tolower(sendme)=="q"){
      break
    }
	sendme <- paste(sendme, strrep(" ", HEADER - nchar(sendme)), sep = "")
    while (TRUE){
		writeChar(sendme, con)
    	server_resp <- trimws(readChar(con, HEADER))
    	print(paste("Your upper cased text:  ", server_resp))
	}
    close(con)
}
client()