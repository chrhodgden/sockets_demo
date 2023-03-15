from ast import literal_eval

cls_str = type("string")

data = "hello"

if type(data) == cls_str:

	n = ""
	print(data, type(data))

	for s in data:
		m = ord(s)
		m = hex(m)
		n += m.lstrip('0x')

	print(n, type(n))

	data = n
	print(data, type(data))

	data = int(data, 16)
	print(data, type(data))

	data = bin(data)
	print(data, type(data))

	data = data.lstrip('0b')
	print(data, type(data))

	data = data.zfill(8)
	print(data, type(data))

	data = int(data, 2)
	print(data, type(data))

	data = hex(data)
	print(data, type(data))

	data = data.lstrip('0x')
	print(data, type(data))

	data = bytearray.fromhex(data)
	print(data, type(data))

	data = data.decode()
	print(data, type(data))
