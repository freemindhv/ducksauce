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
    def __init__(self, constructor_table = {}):
        self.c = constructor_table
    
    def deserialize(self, s):
        attr = json.loads(s).decode();
        
        return self.c[attr[0]](attr)
        
        