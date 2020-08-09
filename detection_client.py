import socket

#modulo de Hamming
from funciones import codigoHamming

#modulo de Fletcher
from fletcher import generateFletcherChecksum

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

msg = s.recv(1024)
msg.decode('UTF-8')

mensaje_esperado = "hola"
mensaje_recibido = msg.decode('UTF-8')

print('mensaje_esperado: ',mensaje_esperado)
print('mensaje_recibido: ',mensaje_recibido)
#
# print('Hamming: ')
# codigoHamming(mensaje_recibido, mensaje_esperado)

print('Fletcher orignal: ')
generateFletcherChecksum(mensaje_esperado)

print('Fletcher recibido: ')
generateFletcherChecksum(mensaje_recibido)
