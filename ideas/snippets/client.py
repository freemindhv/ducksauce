#!/usr/bin/env python3

# Echo client program
import socket
import JSONTest
host = "localhost"        # The remote host
port = 51001              # The same port as used by the server
data = JSONTest.Message01("Here comes a shitload of data")

#convert to JSON
x = data.toJSONString()
y = JSONTest.Message02(1000, ["", "", ""]).toJSONString().encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(x.encode())
s.sendall(y)
s.close()
print("Data succesfully send")
