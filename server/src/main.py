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

from modules.serversocket import ServerSocket as ServerSocket
from modules.objects import MessageHandler as MessageHandler
from modules.serial import Decoder as Decoder
from modules.messages import MessageId as MessageId
from modules.messages import Ping as Ping
from modules.messages import Acknowledgement as Acknowledgement
from modules.messages import BillRequest as BillRequest
from modules.messages import BillResponse as BillResponse
from modules.messages import ReserveTableRequest as ReserveTableRequest

def handlePing(msg):
    print("handling Ping")
    
def handleAck(msg):
    print("handling Ack")
   
def handleBillRequest(msg):
    print("handling BillRequest")
    
def handleBillResponse(msg):
    print("handling BillResponse")
    
def handleOrderRequest(msg):
    print("handling OrderRequest")
    
def handleReserveTableRequest(msg):
    print("handling ReserveTableRequest")

def setupMessageHandler():
    decoder_table = {
        MessageId.PING : Ping.fromAttributeList,
        MessageId.ACKNOWLEDGEMENT : Acknowledgement.fromAttributeList,
        MessageId.BILL_REQUEST : BillRequest.fromAttributeList,
        MessageId.BILL_RESPONSE : BillResponse.fromAttributeList,
        MessageId.RESERVE_TABLE_REQUEST : ReserveTableRequest.fromAttributeList
    }
    
    decoder = Decoder(decoder_table)
    
    handler_table = {
        MessageId.PING : handlePing,
        MessageId.ACKNOWLEDGEMENT : handleAck,
        MessageId.BILL_REQUEST : handleBillRequest,
        MessageId.BILL_RESPONSE : handleBillResponse,
        MessageId.RESERVE_TABLE_REQUEST : handleReserveTableRequest
    }
    
    return MessageHandler(decoder, handler_table)

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
                else:
                    print("Client disconnected")
                    x.close()
                    reading.remove(x)
                
