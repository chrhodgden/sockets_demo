#library(R.utils)

data <- "e"
#data <- as.integer(256)
cat(data, typeof(data), "\n")

if(is.character(data)){

	data <- charToRaw(data)
	cat(data, typeof(data), "\n")

	#data <- strtoi(data, 16L)
	n <- strtoi(data, 16L)
	cat(n, typeof(n), "\n")

	#data <- intToBin(data)
	#data <- intToBits(data)
	data <- rawToBits(data)
	cat(data, typeof(data), "\n")

	#data <- strtoi(data, 2)
	#cat(data, typeof(data), "\n")

	#data <- as.raw(data)
	data <- packBits(data, "raw")
	cat(data, typeof(data), "\n")

	data <- rawToChar(data)
	cat(data, typeof(data), "\n")

}else if(is.integer(data)){

	data <- as.raw(data)
	cat(data, typeof(data), "\n")

	data <- rawToBits(data)
	cat(data, typeof(data), "\n")

	data <- packBits(data, "raw")
	cat(data, typeof(data), "\n")

	data <- as.integer(data)
	cat(data, typeof(data), "\n")
}