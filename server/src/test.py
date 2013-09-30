from modules.messages import MessageId as MessageId
from modules.messages import ReserveTableRequest as ReserveTableRequest
from modules.messages import BillResponse as BillResponse
from modules.serial import Decoder as Decoder
from modules.objects import Order as Order

msg_constructors = {
    MessageId.RESERVE_TABLE_REQUEST : ReserveTableRequest.fromAttributeList,
    MessageId.BILL_RESPONSE : BillResponse.fromAttributeList
}

decoder = Decoder(msg_constructors)

s1 = ReserveTableRequest(3, 8, 800, 2.45).serialize()

print(s1)

decoded1 = decoder.deserialize(s1)

print(str(decoded1.id))
print(str(decoded1.table_num))
print(str(decoded1.seats))
print(str(decoded1.time))
print(str(decoded1.duration))

s2 = BillResponse(["Cola", "Pizza", "Hefeweizen", "Muscheln"], 21.99).serialize()

print(s2)

decoded2 = decoder.deserialize(s2)

print(str(decoded2.id))

print(*decoded2.order.items)
    
print(str(decoded2.sum))