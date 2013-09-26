#!/usr/bin/python 
# Echo client program
import socket

HOST = 'localhost'    	  # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(bytes('Hello, world', "utf-8"))
data = s.recv(1024)
s.close()
print("Received: {}".format(data.decode("utf-8")))