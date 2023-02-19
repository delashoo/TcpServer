#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()

port = 444

clientsocket.connect(('IP',port))

message = clientsocket.receive(1023)

clientsocket.close()

print(message.decode('ascii'))