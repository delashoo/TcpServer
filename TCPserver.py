#!/usr/bin/python3

import socket #Importing the socket module from Python

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initializing socket function, specifying parameters (the socket family & socket type)
#SOCK_STREAM is for specifying connection-oriented protocols

host = socket.gethostbyname()
port = 444

serversocket.bind((host, port)) # Binding the host and port to the socket

serversocket.listen(3) #Starts the TCP listener

while True:
    clientsocket, address = serversocket.accept() #Allows for acceptance of Tcp info

    print("received connection from" % str(address))

    message = "Hello! Thank you for connecting to the server" + "\r\n"
    clientsocket.send(message) #sends a TCP message

    clientsocket.close() #ends connection