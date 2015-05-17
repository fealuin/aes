import socket
import sys



while(True):
	sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('localhost',8888))

	msg=raw_input("Escriba su mensaje")
	if msg:
		sock.sendall(msg)
	sock.close()