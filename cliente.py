import socket
import sys

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',8888))

while(True):


	msg=raw_input("Escriba su mensaje:\n")
	
	sock.sendall(msg)

sock.close()