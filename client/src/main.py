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
##!/usr/bin/env python3

from modules.clientsocket import ClientSocket as ClientSocket
from modules.serial import Encoder as Encoder

client_socket = ClientSocket("127.0.0.1", 51001) #localhost for testing purposes

#convert a testing message to JSON
msg = ("Here comes a shitload of data")

client_socket.send(msg.serialize)