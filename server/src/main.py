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
reading = [a.s]

while 1:
    inputready,outputready,exceptready = select.select(reading,[],[]) 
    for x in inputready:
        if x == a.s:
            conn,addr = x.accept()
            reading.append(conn)
            print("Conecction established by {}" .format(addr))
        else:
            data = x.recv(buffsize)
            if data:
                print("Data is received as follows:{}" .format(data))
            else:
                print("Client disconnected")
                x.close()
                reading.remove(x)
                
a.s.close()
