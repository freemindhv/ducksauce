#!/usr/bin/env python3
import socket
import select

host = socket.gethostbyname(socket.gethostname())
port = 51001
buffsize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    s.bind((host,port))
except socket.error as msg:
    print("Could not open socket, maybe the port is already used?")
s.listen(5)

while True:
    inputready,outputready,exceptready = select.select([s],[],[]) 
    for x in inputready:
        if x == s:
            conn,addr = s.accept()
        else:
            data = s.recv(buffsize)
            if data:
                print(data)
            else:
                x.close()
                
s.close()