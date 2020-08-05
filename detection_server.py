import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

#listen forever
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} succesful!")
    clientsocket.send(bytes('test message','utf-8'))
