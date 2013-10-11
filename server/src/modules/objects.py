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


class Table:
    def __init__(self, id, capacity):
        self.id = id
        self.cap = capacity
        self.active_order = []
        self.reservations = None
        self.log = None
        self.occupied = None
        
    def attributeList(self):
        return [self.id, self.cap]
    
    def addOrder(self, item):
        self.active_order.append(item)
        
    def deleteOrder(self, item):
        self.active_order.remove(item)
        
    def order(self):
        return self.active_order
    
    def clearActiveOrder(self):
        self.active_order = []


# TODO: finish class
class Client:
    def __init__(self):
        self.id = 0