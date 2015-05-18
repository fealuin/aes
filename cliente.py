import socket
import sys
import cfb
import log

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=raw_input("Escriba host del servidor:")
try:
    sock.connect((host,8888))
except:
    print("host no encontrado")
    exit()
    print("Se ha establecido conexion con el servidor, para salir ingrese un mensaje vacio")
while(True):
    msg=raw_input("Escriba su mensaje:\n")
    if len(msg)%2: msg=msg+' '
    if not msg: 
        break
    iv=(raw_input("Escriba Vector Inicial:\n")+" "*16)[:16]
    k=(raw_input("Escriba clave:\n")+" "*16)[:16]
    log.logreset()
    sock.sendall(str(len(msg)))
    cfb.enviocfb(msg,k,iv,sock)
    
sock.sendall('0')
print "Saliendo"
sock.close()