con2 <- socketConnection(Sys.info()["nodename"], port = 6011)
# as non-blocking, may need to loop for input
con2
readLines(con2)
while(isIncomplete(con2)) {
   #Sys.sleep(1)
   z <- readLines(con2)
   if(length(z)) print(z)
}
close(con2)