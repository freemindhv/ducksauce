#!/usr/bin/env python3

#
# This file is part of ducksauce.
#
# Ducksauce is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ducksauce is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar. If not, see <http://www.gnu.org/licenses/>.
#

import select

from modules.network import ServerSocket as ServerSocket
from modules.network import MessageHandler as MessageHandler
from modules.network import MessageId as MessageId
from modules.network import Ping as Ping
from modules.network import Ack as Ack
from modules.network import RegistrationRequest as RegistrationRequest
from modules.network import BillRequest as BillRequest
from modules.network import BillResponse as BillResponse
from modules.network import OrderRequest as OrderRequest
from modules.network import ReserveTableRequest as ReserveTableRequest

from modules.objects import Client as Client

def handlePing(client, msg):
    print("handling Ping\nId: {}".format(msg.id))
    
    response = Ack(0).serialize()
    
    client.send(response)
    
    return True
    
    
def handleAck(client, msg):
    print("handling Ack\nId: {}\nError: {}".format(msg.id, msg.err))


def handleRegistrationRequest(client, msg):
    print("handling RegistrationRequest\nId: {}".format(msg.id))
    
    client.register()
    
    response = Ack(0).serialize()
    
    client.send(response)
    
    return True
   
   
def handleBillRequest(client, msg):
    print("handling BillRequest\nId: {}\nTableId: {}".format(msg.id, msg.table_num))
    
    response = BillResponse(["Beer", "Pizza"], 10.99).serialize()
    
    client.send(response)
    
    
def handleOrderRequest(client, msg):
    print("handling OrderRequest\nId: {}".format(msg.id))
    
    
def handleReserveTableRequest(client, msg):
    print("handling ReserveTableRequest\n                                      \
        Id: {}\n                                                               \
        TableId: {}\n                                                          \
        Seats: {}\n                                                            \
        Time: {}\n                                                             \
        Duration: {}".format(msg.id, msg.table_num, msg.time, msg.duration))


def setupMessageHandler():
    handler = MessageHandler()
    
    handler.addHandler(MessageId.PING, handlePing)
    handler.addHandler(MessageId.ACK, handleAck)
    handler.addHandler(MessageId.BILL_REQUEST, handleBillRequest)
    handler.addHandler(MessageId.ORDER_REQUEST, handleOrderRequest)
    handler.addHandler(MessageId.RESERVE_TABLE_REQUEST, handleReserveTableRequest)
    
    return handler


if __name__ == "__main__":
    
    message_handler = setupMessageHandler()
    
    server_sock = ServerSocket("", 51001)
    reading = [server_sock.socket()]
    
    client_table = {}

    while 1:
        inputready,outputready,exceptready = select.select(reading, [], [])
        for x in inputready:

            # add new connection
            if x == server_sock.socket():
                conn,addr = x.accept()
                
                fd = conn.fileno()
                
                client_table[fd] = Client(conn, addr)
                reading.append(conn)
                
                print("Connection established by {}".format(addr))
                continue
            
            fd = x.fileno()

            # receive message and handle it
            client = client_table[fd]
            s = client.recv(4096)
            
            if not s:
                print("Client {} disconnected".format(client.address()))
                
                del client_table[fd]
                reading.remove(x)
                continue
                
            print("Received: {}".format(s.decode()))
            
            ok = message_handler.handleMessage(client, s)
            
            if not ok:
                if not client.isRegistered():
                    reading.remove(x)
                    del client_table[fd]
                else:
                    client.createdError()


                
