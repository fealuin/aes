import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (('localhost', 8888))
print 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)
while True:
    # Wait for a connection
    print >>sys.stderr, 'Esperando por una coneccion'
    connection, client_address = sock.accept()


    while True:
        data = connection.recv(1024)
        
        if data:
            print >>sys.stderr, 'received "%s"' % data
        

connection.close()
