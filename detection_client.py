import socket
from funciones import codigoHamming

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

msg = s.recv(1024)
print(msg.decode('UTF-8'))

mensaje_esperado = "hola"
mensaje_recibido = msg.decode('UTF-8')

codigoHamming(mensaje_recibido, mensaje_esperado)
