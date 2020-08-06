import socket
import bitarray
from funciones import ruido

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

message = "hola"

ba = bitarray.bitarray()
ba.frombytes(message.encode('utf-8'))
ba_ruido = ruido(ba, 1, 100)

#listen forever
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} succesful!")
    clientsocket.send(ba_ruido)
