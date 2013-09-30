#!/usr/bin/env python3

#
#    This file is part of ducksauce.
#
#    Ducksauce is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Ducksauce is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

import select
import modules.socketlib

#host = socket.gethostbyname(socket.gethostname())
host = ""
port = 51001
buffsize = 1024
backlog = 5
print(host)

a = modules.socketlib.DsSocket(host, port, backlog)
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
