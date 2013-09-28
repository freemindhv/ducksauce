#!/usr/bin/env python3
import socket

class DsSocket:
    def __init__(self, host, port, backlog = 5):
        self.h = host
        self.p = port
        self.b = backlog
        
    def socketInit(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.setblocking(0)
    
    def socketBind(self):
        try:
            self.s.bind((self.h,self.p))
        except socket.error as msg:
            print("Could not open socket, maybe the port is already used?")
            print("Error was {}" .format(msg))
        self.s.listen(self.b)