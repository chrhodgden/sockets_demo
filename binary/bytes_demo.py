# bytes vs bytearray
mybytes = bytes([0, 1, 3, 4])
print(mybytes)

#cannot change single value. Not an iterable
#mybytes[2] = 4
print(type(mybytes[2]), mybytes[2])

myByteArray = bytearray(mybytes)
myByteArray[2] = 4
print(type(myByteArray), myByteArray)

mybytes = bytes(myByteArray) 
print(type(mybytes), mybytes)

myInts = [x for x in myByteArray]
print(type(myInts), myInts)

myInts = [x for x in mybytes]
print(type(myInts), myInts)

myInts = list(myByteArray)
print(type(myInts), myInts)

myInts = list(mybytes)
print(type(myInts), myInts)

myByteArray = bytearray([0, 1, 3, 4])
print(type(myByteArray), myByteArray)
