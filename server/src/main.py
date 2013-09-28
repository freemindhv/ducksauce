#!/usr/bin/env python3
import socket
import select
import socketlib

host = socket.gethostbyname(socket.gethostname())
port = 51001
buffsize = 4096
backlog = 5

a = socketlib.DsSocket(host, port, backlog)
a.socketInit()
a.socketBind()

while True:
    inputready,outputready,exceptready = select.select([a.s],[],[]) 
    for x in inputready:
        if x == a.s:
            conn,addr = a.s.accept()
        else:
            data = a.s.recv(buffsize)
            if data:
                print(data)
            else:
                x.close()
                
a.s.close()