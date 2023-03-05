con1 <- socketConnection(
		port = 6011,
		server = TRUE,
		encoding = "UTF-8"
)
writeLines(LETTERS, con1)
close(con1)