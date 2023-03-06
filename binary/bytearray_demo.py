# bytes vs bytearray
mybytes = bytes([1, 2, 3, 4])
print(mybytes)

#cannot change single value. Not an iterable
#mybytes[2] = 4

myByteArray = bytearray(mybytes)
myByteArray[2] = 4
print(myByteArray)

