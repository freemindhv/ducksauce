


import json

class JSONMessageSerializer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Message01):
            return [obj.id, obj.data]
        elif isinstance(obj, Message02):
            return [obj.id, obj.data1, obj.data2]

        return json.JSONEncoder.default(self, obj)

def asMessage(dct):
    if isinstance(obj, Message01):
        return Message01(dct['id'], dct['data'])
    elif isinstance(obj, Message02):
        return Message02(dct['id'], dct['data1'], dct['data2'])
    else:
        return None

class Message01:
    def __init__(self, header = None, data=None):
        self.id   = header
        self.data = data

    def dump(self):
        print("Message01: " + str(self.id) + " " + self.data)
    @staticmethod
    def fromJSONString(s):
        x = json.loads(s);

        return Message01(x[0], x[1])

class Message02:
    def __init__(self, header = None, data1 = None, data2 = None):
        self.id = header
        self.data1 = data1
        self.data2 = data2
    def dump(self):
        print("Message02: " + str(self.id) + " " + self.data1 + " ")
        for item in self.data2:
            print(item + " ")

    @staticmethod
    def fromJSONString(s):
        x = json.loads(s)

        return Message02(x[0], x[1], x[2])

if __name__ == "__main__":

    msg01 = Message01(0xff, "Message Data")


    s = json.dumps(msg01, cls = JSONMessageSerializer)

    msg01 = Message01.fromJSONString(s)

    msg01.dump()


    msg02 = Message02(0xfe, "Data", ["DataXX. DataYY"])

    s = json.dumps(msg02, cls = JSONMessageSerializer)

    msg02 = Message02.fromJSONString(s)

    msg02.dump()
