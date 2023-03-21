bitToStr <- function(data) return(rawToChar(packBits(data, "raw")))
strToBit <- function(data) rawToBits(charToRaw(data))