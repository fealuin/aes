import socket
import sys
import cfb

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost',8888))

while(True):
    msg=(raw_input("Escriba su mensaje:\n")+" "*16)[:16]
    iv=(raw_input("Escriba Vector Inicial:\n")+" "*16)[:16]
    k=(raw_input("Escriba clave:\n")+" "*16)[:16]
    sock.sendall('1')
    cfb.enviocfb(msg,k,iv,sock)
    

sock.close()