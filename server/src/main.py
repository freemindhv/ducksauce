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
from modules.network import Acknowledgement as Acknowledgement
from modules.network import BillRequest as BillRequest
from modules.network import BillResponse as BillResponse
from modules.network import OrderRequest as OrderRequest
from modules.network import ReserveTableRequest as ReserveTableRequest


def handlePing(msg):
    print("handling Ping\nId: {}".format(msg.id))
    
def handleAck(msg):
    print("handling Ack\nId: {}\nError: {}".format(msg.id, msg.err))
   
def handleBillRequest(msg):
    print("handling BillRequest\nId: {}\nTableId: {}".format(msg.id, msg.table_num))
    
def handleBillResponse(msg):
    print("handling BillResponse\nId: {}".format(msg.id))
    print(msg.order)
    print("sum: {}".format(msg.sum))
    
def handleOrderRequest(msg):
    print("handling OrderRequest\nId: {}".format(msg.id))
    
def handleReserveTableRequest(msg):
    print("handling ReserveTableRequest\n       \
        Id: {}\n    \
        TableId: {}\n    \
        Seats: {}\n    \
        Time: {}\n    \
        Duration: {}".format(msg.id, msg.table_num, msg.time, msg.duration))

def setupMessageHandler():
    handler = MessageHandler()
    
    handler.addHandler(MessageId.PING, handlePing)
    handler.addHandler(MessageId.ACKNOWLEDGEMENT, handleAck)
    handler.addHandler(MessageId.BILL_REQUEST, handleBillRequest)
    handler.addHandler(MessageId.BILL_RESPONSE, handleBillResponse)
    handler.addHandler(MessageId.ORDER_REQUEST, handleOrderRequest)
    handler.addHandler(MessageId.RESERVE_TABLE_REQUEST, handleReserveTableRequest)
    
    return handler

if __name__ == "__main__":
    
    message_handler = setupMessageHandler()
    
    server_sock = ServerSocket("", 51001)
    reading = [server_sock.fd()]
    

    while 1:
        inputready,outputready,exceptready = select.select(reading, [], [])
        for x in inputready:
            if x == server_sock.fd():
                conn,addr = x.accept()
                reading.append(conn)
                print("Connection established by {}" .format(addr))
            else:
                s = x.recv(4096)
                if s:
                    print("Received: {}" .format(s.decode()))
                    message_handler.handleMessage(s)

                    m = BillResponse(["Cola", "Kaffee", "Pizza"], 12.99)
                    x.send(m.serialize())
                else:
                    x.close()
                    reading.remove(x)
                    print("Client disconnected")
                
