from ast import literal_eval

cls_str = type("string")
cls_byt = type(b'\x00')

data = b'\x00\x00\x00\x01\x00\x01\x01\x00'
data = '!DIS'

if type(data) == cls_byt:

	print(data, type(data))

	n = ""
	for b in data: n = f'{b}{n}'
	data = n
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

elif type(data) == cls_str:

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

	n = b''
	for b in data:
		m = int(b)
		m = chr(m)
		m = bytes(m, 'utf-8')
		print(m, type(m))
		n += m

	data = n
	print(data, type(data))

	n = ""
	for b in data: n = f'{n}{b}'
	data = n
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
