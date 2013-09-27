#!/usr/bin/python 

# Echo server program
import socket

host = '0.0.0.0'          # Symbolic name meaning all available interfaces
port = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print("Connected by {}".format(str(addr)))
while 1:
    data = conn.recv(1024)
    if not data: break
    print(data.decode("utf-8"))
conn.close()
