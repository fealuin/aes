import socket
import sys
import aes

def enviar(msg,sock):
    sock.sendall(msg)

def textoALista(texto):
    l=[]
    for i in range(16):
        l.append(ord(texto[i]))
    return l

def enviocfb(texto,k,iv,sock):
    textoInt=textoALista(texto)
    for i in range(8):
        c=aes.encriptarAes(iv,k)
        c=chr(ord(c[0])^textoInt[i*2])+chr(ord(c[1])^textoInt[i*2+1])
        iv=iv[2:]+c
        enviar(c,sock)


def reccfb(k,iv,connection):
    texto=''
    for i in range(8):
        r=aes.encriptarAes(iv,k)
        c=connection.recv(2)
        p=chr(ord(c[0])^ord(r[0]))+chr(ord(c[1])^ord(r[1]))
        texto=texto+p
        iv=iv[2:]+c
    print "Se ha recibido %s"%texto