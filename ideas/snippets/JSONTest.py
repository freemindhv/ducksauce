#!/usr/bin/python

import json

class JSONMessageEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Message01):
            return [obj.id, obj.data]
        elif isinstance(obj, Message02):
            return [obj.id, obj.val, obj.strings]
        else:
            return json.JSONEncoder.default(self, obj)

class MessageHandler:
    def __init__(self):
        self.table = {}

    def setHandler(self, msgId, handler):
        self.table[msgId] = handler
 
    def handleMessage(self, s):
        val = json.loads(s)

        self.table[val[0]](val)

def handleMessage01(s):
    msg = Message01.fromJSONList(s)
    print("MessageHandler for Message01 active:")
    msg.dump()

def handleMessage02(s):
    msg = Message02.fromJSONList(s)
    print("MessageHandler for Message02 active:")
    msg.dump()

class Message:
    @staticmethod
    def fromJSONList(s):
        raise NotImplementedError("Subclasses must implement this function")
    def toJSONString(self):
        return json.dumps(self, cls = JSONMessageEncoder)

class Message01(Message):
    def __init__(self, data = None):
        self.id   = 0x01
        self.data = data

    def dump(self):
        print("Message01: " + str(self.id) + " " + self.data + "\n")

    @staticmethod
    def fromJSONList(s):
        return Message01(s[1])

class Message02(Message):
    def __init__(self, val = None, strings = None):
        self.id = 0x02
        self.val = val
        self.strings = strings

    def dump(self):
        print("Message02: " + str(self.id) + " " + str(self.val) + " " + " ".join(self.strings) + "\n")
        
    @staticmethod
    def fromJSONList(s):
        return Message02(s[1], s[2])

if __name__ == "__main__":

    msghandler = MessageHandler()

    msghandler.setHandler(0x01, handleMessage01)
    msghandler.setHandler(0x02, handleMessage02)

    msg01 = Message01("A hole bunch of data")
    x = msg01.toJSONString()
    msghandler.handleMessage(x)

    msg02 = Message02(10, ["God", "damnit", "Larry"])
    y = msg02.toJSONString()
    msghandler.handleMessage(y)
