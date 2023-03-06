import struct

FORMAT = 'i 4s f'

data = (10, b'Code', 2022)

print(data)

packedData = struct.pack(FORMAT, *data)
print(packedData)

unpackedData = struct.unpack(FORMAT, packedData)
print(unpackedData)

