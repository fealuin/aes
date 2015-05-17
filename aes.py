##MATRICES

# caja de sustitucion
sbox =  [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
    0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
    0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
    0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
    0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
    0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
    0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
    0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
    0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
    0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
    0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
    0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
    0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
    0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
    0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
    0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
    0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
    0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
    0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
    0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
    0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
    0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
    0x54, 0xbb, 0x16]

# caja de sustirucion inversa
rsbox = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
    0x9e, 0x81, 0xf3, 0xd7, 0xfb , 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
    0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb , 0x54,
    0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
    0x42, 0xfa, 0xc3, 0x4e , 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
    0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25 , 0x72, 0xf8,
    0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
    0x65, 0xb6, 0x92 , 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
    0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84 , 0x90, 0xd8, 0xab,
    0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
    0x45, 0x06 , 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
    0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b , 0x3a, 0x91, 0x11, 0x41,
    0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
    0x73 , 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
    0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e , 0x47, 0xf1, 0x1a, 0x71, 0x1d,
    0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b ,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
    0xfe, 0x78, 0xcd, 0x5a, 0xf4 , 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
    0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f , 0x60,
    0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
    0x93, 0xc9, 0x9c, 0xef , 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
    0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61 , 0x17, 0x2b,
    0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
    0x21, 0x0c, 0x7d]

# tabla rcon
Rcon = [
      [0x01,0,0,0],
      [0x02,0,0,0],
      [0x04,0,0,0],
      [0x08,0,0,0],
      [0x10,0,0,0],
      [0x20,0,0,0],
      [0x40,0,0,0],
      [0x80,0,0,0],
      [0x1b,0,0,0],
      [0x36,0,0,0],
      ]

#Matriz mix columns
mix=[
      [2,3,1,1],
      [1,2,3,1],
      [1,1,2,3],
      [3,1,1,2]
      ]
#Matriz mix columns inversa
imix=[
      [14,11,13,9],
      [9,14,11,13],
      [13,9,14,11],
      [11,13,9,14]
      ]
import string

##OPERACIONES BASICAS
#Imprime matriz en formato hexadecimal
def imprimeMatrizHex(matriz):
      for filas in matriz:
            print "\n"
            for columnas in filas:
                  print "%02x"%columnas,
      print "\n"

#Toma el texto claro, lo deja en una matriz por columnas convirtiendo cada caracter a int
def textoAEstado(texto): 
      matriz=[range(4) for i in range(4)]
      for i in range(16):
            matriz[i%4][i/4]=ord(texto[i])
      return matriz
#Toma una matriz de estado y la lleva a texto por columnas
def estadoAtexto(estado): 
      texto=""
      for i in range(4):
            for j in xrange(4):
                  texto+=chr(estado[j][i])
      return texto

#Toma clave y la lleva a una matriz por filas (orden ppt vista en clases)
def textToClave(texto): 
      matriz=[range(4) for i in range(4)]
      for i in range(16):
            matriz[i/4][i%4]=ord(texto[i])
      return matriz

##OPERACIONES AES
#Hace un XOR entre la matriz de estado y una clave
def addRoundKey(estado,k):
      for i in range(4):
            for j in range(4):
                  estado[i][j]=estado[i][j]^k[i][j]
      return estado

#Substituye elementos de estado en matriz de substitucion
def byteSub(estado,matriz):
      for i in range(4):
            for j in range(4):
                  estado[i][j]=matriz[estado[i][j]]
      return estado
#Rota filas de la columna estado 0,1,2,3 a la izquierda
def shiftRows(estado):
      for i in range(4):
            estado[i]=estado[i][i:]+estado[i][:i]
      return estado
#Rota filas de la columna estado 0,1,2,3 a la derecha
def invShiftRows(estado):
      for i in range(4):
            estado[i]=estado[i][-i:]+estado[i][:-i]
      return estado

#Para multGalois se utilizo el siguiente algoritmo, disponible en http://samiam.org/galois.html
#Take two eight-bit numbers, a and b, and an eight-bit product p
#Set the product to zero.
#Make a copy of a and b, which we will simply call a and b in the rest of this algorithm
#Run the following loop eight times:
#If the low bit of b is set, exclusive or the product p by the value of a
#Keep track of whether the high (eighth from left) bit of a is set to one
#Rotate a one bit to the left, discarding the high bit, and making the low bit have a value of zero
#If a's hi bit had a value of one prior to this rotation, exclusive or a with the hexadecimal number 0x1b
#Rotate b one bit to the right, discarding the low bit, and making the high (eighth from left) bit have a value of zero.
#The product p now has the product of a and b

def multGalois(x,y):
      p=0
      a=x
      b=y
      for i in range(8):
            if b&0b00000001: #Si b tiene el bit menos significativo = 1 a XOR p
                  p=p^a
            hia=a&0b10000000 #Guardamos el bit mas significativo de a antes de rotar a
            
            a=a<<1
            a%256 #Se eliminan bits > 8
            if hia==0b10000000:
                  a=a^0x1b
            b=b>>1
      return p%256


#Opera multiplica una matriz por el vector columna en un espacio finito
def mixColumn(columna,matriz):
      aux=[0,0,0,0]
      for i in range(4):
            for j in range(4):
                  mult=multGalois(matriz[i][j],columna[j])
                  aux[i]^=mult
      return aux
#multiplica todas las columnas del estado con matriz
def mixColumns(estado,matriz):
      aux=[0,0,0,0]
      for i in range(4):
            for j in range(4):
                  aux[j]=estado[j][i]
            aux=mixColumn(aux,matriz)
            for k in range(4):
                  estado[k][i]=aux[k]
      return estado

##OPERACIONES DE CLAVE
# reemplaza elementos de un vector en caja de sustitucion sbox
def subByte(fila):
      for i in range(4):
            fila[i]=sbox[fila[i]]
      return fila
#Rota vector 1 a la izquierda
def rotByte(fila):
      fila=fila[1:]+fila[:1]
      return fila
#hace un XOR con los elementos de dos vectore
def xorFilaFila(fila1,fila2):
      aux=[]
      for i in range(4):
            aux.append(fila1[i]^fila2[i])
      return aux
#expande clave
def expandeClave(k):
      clave=textToClave(k)
      #print "Expandiendo clave",k
      
      for i in range(4,44):
            aux=clave[i-1]
            if(i%4==0):
                  aux=xorFilaFila(subByte(rotByte(aux)),Rcon[i%4])
            clave.append(xorFilaFila(clave[i-4],aux))
      #imprimeMatrizHex(clave)
      return clave
#busca en la clave expandida la clave que corresponde a cada ronda
def seleccionaClave(k,ronda):
      #print "Seleccionando RoundKey",ronda
      subclave=k[ronda*4:ronda*4+4]
      #imprimeMatrizHex (subclave)
      return subclave

##ENCRIPTACION
#Ronda encriptacion
def rondaAes(estado,k):
      byteSub(estado,sbox)
      shiftRows(estado)
      mixColumns(estado,mix)
      addRoundKey(estado,k)

#Encriptacion AES
def encriptarAes(texto,k):
      #ronda inicial
      estado=textoAEstado(texto)
      clave=expandeClave(k)
      addRoundKey(estado,seleccionaClave(clave,0))
      for i in range(1,10):
            rondaAes(estado, seleccionaClave(clave,i))
      #Ronda final
      byteSub(estado,sbox)
      shiftRows(estado)
      addRoundKey(estado,seleccionaClave(clave,10))
      return estadoAtexto(estado)

#DESENCRIPTACION
#Ronda desencriptacion
def rondaAesInv(estado,k):
      addRoundKey(estado,k)
      mixColumns(estado,imix)
      invShiftRows(estado)
      byteSub(estado,rsbox)

#Desencriptacion
def desencriptarAes(texto,k):
      estado=textoAEstado(texto)
      clave=expandeClave(k)
      #Ronda Inicial
      addRoundKey(estado,seleccionaClave(clave,10))
      #print "Antes de shift rows",estado
      invShiftRows(estado)
      #print "Despues de shift rows",estado
      byteSub(estado,rsbox)
      for i in range(9,0,-1):
            rondaAesInv(estado,seleccionaClave(clave,i))
      addRoundKey(estado,seleccionaClave(clave,0))
      return estadoAtexto(estado)


#texto="La casa es chica"
#estado=textoAEstado(texto)
#print estadoAtexto(estado)
#imprimeMatrizHex(estado)
#print "texto encriptado:" + encriptarAes("La casa es chica","Eres Informatico")
#a=encriptarAes("La casa es chica","Eres Informatico")
#print "casi desencriptado: "+desencriptarAes(a,"Eres Informatico")
#imprimeMatrizHex(encriptarAes("La casa es chica","Eres Informatico"))
#imprimeMatrizHex( expandeClave("Eres Informatico"))

#addRoundKey(addRoundKey(textoAEstado(texto),textoAEstado("1234567890123456")),textoAEstado("1234567890123456"))
#shiftRows(estado)
#byteSub(estado)
#print estado
#print bin(multGalois(2,0xd4))
#columna=[estado[i][0] for i in range(4)]
#columna=mixColumns(estado,mix)
#imprimeMatrizHex(estado)

#for x in range(4):
#     print hex(columna[x]) 