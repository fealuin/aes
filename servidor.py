import socket
import sys
import cfb

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (('localhost', 8888))
print 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)
while True:
    # Wait for a connection
    print >>sys.stderr, 'Esperando por una conexion'
    connection, client_address = sock.accept()
    print "Se ha recibido una conexion desde la direccion:",client_address[0],":",client_address[1]
    while(True):
        inicio=connection.recv(8)
        if inicio=='1': #Inicia la conversacion con un 1
            print("Se esta recibiendo un mensaje\n")
            iv=(raw_input("Escriba Vector Inicial:\n")+" "*16)[:16]
            k=(raw_input("Escriba clave:\n")+" "*16)[:16]
            cfb.reccfb(k,iv,connection)

                

connection.close()
