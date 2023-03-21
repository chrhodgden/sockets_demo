def bitToStr(data):
	n = ''
	for b in data: n = f'{b}{n}'
	return bytearray.fromhex(hex(int(n, 2)).lstrip('0x')).decode()

def strToBit(data):		
	n = ''
	for s in data: n += hex(ord(s)).lstrip('0x')
	data = ''.join(reversed(bin(int(n, 16)).replace('b', '')))
	n = b''
	for b in data: n += bytes(chr(int(b)), 'utf-8')
	return n