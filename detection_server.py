import socket
import bitarray

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

ba = bitarray.bitarray()
message = input("Mensaje a enviar: ")
ba.frombytes(message.encode('utf-8'))

#listen forever
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} succesful!")
    clientsocket.send(ba)
