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

import configparser

class Config:
    def __init__(self, path):
        parser = configparser.ConfigParser()
        
        parser.readfp(open(path, "r"))
        
        self.path_menu = parser.get("ducksauce", "PathMenu")
        self.path_certs = parser.get("ducksauce", "PathCerts")
        self.num_tables = parser.getint("ducksauce", "NumberOfTables")
        
    def pathMenu(self):
        return self.path_menu
    
    def pathCerts(self):
        return self.path_certs
    
    def numberOfTables(self):
        return self.num_tables