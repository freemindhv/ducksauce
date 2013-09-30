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

from modules.serversocket import ServerSocket as ServerSocket

buffsize = 1024

server_sock = ServerSocket("", 51001)
reading = [server_sock.fd()]

while 1:
    inputready,outputready,exceptready = server_sock.select(reading)
    for x in inputready:
        if x == server_sock.fd():
            conn,addr = x.accept()
            reading.append(conn)
            print("Connection established by {}" .format(addr))
        else:
            data = x.recv(buffsize)
            if data:
<<<<<<< HEAD
                print("Data is received as follows:{}" .format(data.decode()))
=======
                print("Received: {}" .format(data.decode()))
>>>>>>> 7149767042a9111873e2deb5b2c94521fe4c90c4
            else:
                print("Client disconnected")
                x.close()
                reading.remove(x)
                
a.s.close()
