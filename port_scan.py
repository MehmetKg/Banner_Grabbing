import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'target_ip'

for port in range (1,100):

	try:
		s.connet((ip,port))
		print(str(port),"open")
	except Exception as e:
		print(str(port),"closed")
	else:
		pass
	finally:
		s.close()