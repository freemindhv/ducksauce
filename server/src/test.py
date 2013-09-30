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

from modules.objects import MessageHandler as MessageHandler
from modules.messages import MessageId as MessageId
from modules.messages import ReserveTableRequest as ReserveTableRequest
from modules.messages import BillResponse as BillResponse
from modules.serial import Decoder as Decoder
#from modules.objects import Order as Order

def handleReserveTableRequest(msg):
    print("handleReserveTableRequest")
    
def handleBillResponse(msg):
    print("handleBillResponse")


d = {
    MessageId.BILL_RESPONSE : BillResponse.fromAttributeList,
    MessageId.RESERVE_TABLE_REQUEST : ReserveTableRequest.fromAttributeList
}

decoder = Decoder(d)

d = {
    MessageId.RESERVE_TABLE_REQUEST : handleReserveTableRequest,
    MessageId.BILL_RESPONSE : handleBillResponse
}

handler = MessageHandler(decoder, d)

s1 = ReserveTableRequest(3, 8, 800, 2.45).serialize()
s2 = BillResponse(["Cola", "Pizza", "Hefeweizen", "Muscheln"], 21.99).serialize()

handler.handleMessage(s1)
handler.handleMessage(s2)