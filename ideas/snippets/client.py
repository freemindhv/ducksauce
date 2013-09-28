#!/usr/bin/env python3

# Echo client program
import socket
import JSONTest
import time
host = "localhost"        # The remote host
port = 51001              # The same port as used by the server

#convert to JSON
x = JSONTest.Message01("Here comes a shitload of data").toJSONString().encode()
y = JSONTest.Message02(1000, ["", "", ""]).toJSONString().encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(x)
s.sendall(y)
time.sleep(5)
s.close()
print("Data succesfully send")
