#!/usr/bin/env python3

import select
import socketlib


#host = socket.gethostbyname(socket.gethostname())
host = ""
port = 51001
buffsize = 1024
backlog = 5
print(host)

a = socketlib.DsSocket(host, port, backlog)
a.socketInit()
a.socketBind()

while 1:
    inputready,outputready,exceptready = select.select([a.s],[],[]) 
    for x in inputready:
        if x == a.s:
            conn,addr = a.s.accept()
            print("Conecction established by {}" .format(addr))
        else:
            data = a.s.recv(buffsize)
            if data:
                print("Data is received as follows:{}" .format(data))
            else:
                x.close()
                
a.s.close()