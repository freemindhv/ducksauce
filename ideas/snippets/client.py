#!/usr/bin/env python

# Echo client program
import socket

host = "localhost"        # The remote host
port = 50007              # The same port as used by the server
data = b"Here comes a bunchload of data"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(data)
s.close()
print("Data succesfully send")

