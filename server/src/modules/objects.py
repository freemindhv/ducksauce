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

class Order(Encoder):
    def __init__(self, items = []):
        self.items = items
        
    def add(self, item):
        self.items.append(item)
        
    def delete(self, item):
        self.items.remove(item)
        
    def attributeList(self):
        return [self.items]

class Table:
    def __init__(self, id, capacity):
        self.id = id
        self.cap = capacity
        self.active_order = Order()
        self.reservations = None
        self.log = None
        self.occupied = None
        
    def attributeList(self):
        return [self.id, self.cap]
    
    def addOrder(self, item):
        self.active_order.add(item)
        
    def deleteOrder(self, item):
        self.active_order.remove(item)
        
    def order(self):
        return self.active_order
    
    def clearActiveOrder(self):
        self.active_order = Order()


class MessageHandler:
    def __init__(self, decoder, handles = {}):
        self.decoder = decoder
        self.handles = handles
        
    def addHandler(self, id, handler):
        self.handles[id] = handler
        
    def removeHandler(self, id):
        del self.handles[id]
        
    def handleMessage(self, msg_string):
        msg_object = self.decoder.deserialize(msg_string);
        
        self.handles[msg_object.id](msg_object)