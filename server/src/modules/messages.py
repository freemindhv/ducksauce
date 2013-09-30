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

from modules.serial import Encoder
from modules.objects import Order

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
    
    @classmethod
    def fromAttributeList(cls, attr):
        return BillResponse(Order(attr[1]), attr[2])
   
   
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