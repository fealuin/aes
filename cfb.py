import socket
import sys
import aes
import log

def enviar(msg,sock):
    sock.sendall(msg)

def textoALista(texto):
    l=[]
    for i in range(len(texto)):
        l.append(ord(texto[i]))
    return l

def enviocfb(texto,k,iv,sock):
    log.tolog("\nIniciando CFB\n Texto:%s\nClave:%s\nIV:%s\n"%(texto,k,iv))
    textoInt=textoALista(texto)
    for i in range(len(textoInt)/2):
        log.tolog("\nEncriptacion CFB\n Clave:%s\nIV:%s\n"%(k,iv))
        c=aes.encriptarAes(iv,k)
        log.tolog("\n %s XOR %s "%(c[0]+c[1],chr(textoInt[i*2])+chr(textoInt[i*2+1])))
        c=chr(ord(c[0])^textoInt[i*2])+chr(ord(c[1])^textoInt[i*2+1])   #XOR dos primeros caracteres
        iv=iv[2:]+c #Rotacion vector
        
        enviar(c,sock)


def reccfb(k,iv,connection,largo):
    log.tolog("\nIniciando desencriptacion CFB\n Clave:%s\nIV:%s\n"%(k,iv))
    texto=''
    for i in range(largo/2):
        r=aes.encriptarAes(iv,k)
        c=connection.recv(2)
        log.tolog("\n %s XOR %s "%(c[0]+c[1],r[0]+r[1]))
        p=chr(ord(c[0])^ord(r[0]))+chr(ord(c[1])^ord(r[1])) #XOR dos primeros caracteres
        texto=texto+p   #Juntando texto
        iv=iv[2:]+c #Rotacion vector
    print "Se ha recibido el mensaje: \"%s\""%texto
    return texto