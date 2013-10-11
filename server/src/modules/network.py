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

import json
import socket
import select

class ServerSocket:
    def __init__(self, host, port, backlog = 5):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.s.bind((host, port))
        except socket.error as msg:
            print("ERROR: bind() failed - {}" .format(msg))

        self.s.listen(backlog)
    
    def __del__(self):
        self.s.close()

    def fd(self):
        return self.s


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Encoder):
            return obj.attributeList()
        else:
            return json.JSONEncoder.default(self, obj)

    def attributeList(self):
        raise NotImplementedError("Subclasses must implement this function")
    
    @classmethod
    def fromAttributeList(cls, attr):
        return cls(*attr[1:])
    
    def serialize(self):
        return json.dumps(self, cls = Encoder).encode()


class Decoder:
    def __init__(self):
        self.c =  {
            MessageId.PING : Ping.fromAttributeList,
            MessageId.ACKNOWLEDGEMENT : Acknowledgement.fromAttributeList,
            MessageId.BILL_REQUEST : BillRequest.fromAttributeList,
            MessageId.BILL_RESPONSE : BillResponse.fromAttributeList,
            MessageId.RESERVE_TABLE_REQUEST : ReserveTableRequest.fromAttributeList
        }
        
    def deserialize(self, s):
        attr = json.loads(s.decode());
        
        return self.c[attr[0]](attr)
    
    def addHandler(self, id, handler):
        self.c[id] = handler

    def removeHandler(self, id):
        del self.c[id]

class MessageId:
    PING = 1
    ACKNOWLEDGEMENT  = 2
    BILL_REQUEST = 3
    BILL_RESPONSE = 4
    ORDER_REQUEST = 5
    RESERVE_TABLE_REQUEST = 6
    
    
class Ping(Encoder):
    def __init__(self):
     self.id = MessageId.PING
     
    def attributeList(self):
         return [self.id]
     
     
class Acknowledgement(Encoder):
    def __init__(self, err):
        self.id = MessageId.ACKNOWLEDGEMENT
        self.err = err
        
    def attributeList(self):
        return [self.id, self.err]


class BillRequest(Encoder):
    def __init__(self, table_num):
        self.id = MessageId.BILL_REQUEST
        self.table_num = table_num
        
    def attributeList(self):
        return [self.id, self.table_num]
    
    
class BillResponse(Encoder):
    def __init__(self, order, sum):
        self.id = MessageId.BILL_RESPONSE
        self.order = order
        self.sum = sum
        
    def attributeList(self):
        return [self.id, self.order, self.sum]
   
   
class ReserveTableRequest(Encoder):
    def __init__(self, table_num, seats, time, duration):
        self.id = MessageId.RESERVE_TABLE_REQUEST
        self.table_num = table_num
        self.seats = seats
        self.time = time
        self.duration = duration
    
    def attributeList(self):
        return [self.id, self.table_num, self.seats, self.time, self.duration]
    
# TODO: finish class   
class OrderRequest(Encoder):
    def __init__(self):
        self.id = MessageId.ORDER_REQUEST  
        
        
class MessageHandler:
    def __init__(self):
        self.decoder = Decoder()
        self.handles =  {}
        
    def addHandler(self, id, handler):
        self.handles[id] = handler
        
    def removeHandler(self, id):
        del self.handles[id]
        
    def handleMessage(self, msg_string):
        msg_object = self.decoder.deserialize(msg_string);
        
        self.handles[msg_object.id](msg_object)