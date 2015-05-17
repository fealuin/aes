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

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            
            if data:
                print >>sys.stderr, 'received "%s"' % data
 
            
    finally:
        # Clean up the connection
        connection.close()
