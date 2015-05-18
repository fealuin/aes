import socket
import sys
import cfb
import log

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (('', 8888))
print 'Iniciando servidor %s en puerto %s' % server_address
sock.bind(server_address)
sock.listen(1)
while True:
    print >>sys.stderr, 'Esperando por una conexion'
    connection, client_address = sock.accept()
    print "Se ha recibido una conexion desde la direccion:",client_address[0],":",client_address[1]
    while(True):
        inicio=int(connection.recv(1024))
        if inicio>0: #Inicia la conversacion con en largo del mensaje, si es 0 se sale
            print("Se esta recibiendo un mensaje\n")
            iv=(raw_input("Escriba Vector Inicial:\n")+" "*16)[:16]
            k=(raw_input("Escriba clave:\n")+" "*16)[:16]
            cfb.reccfb(k,iv,connection,inicio)
        else:
            break
    if(inicio==0):break
                
print("El cliente se ha desconectado, saliendo..")
connection.close()
