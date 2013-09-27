#!/usr/bin/python 
# Echo client program
import socket

HOST = ''                 # The remote host
PORT = 50007              # The same port as used by the server
data = 'Here comes a bunchload of data, 1101010101001101010101010101010101010101010101010010101010101010101010101010'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(data)
s.close()
print 'Data succesfully send'

