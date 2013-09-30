#!/usr/bin/env python3

import socket
import select

class ServerSocket:
    def __init__(self, host, port, backlog = 5):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.s.bind((host, port))
        except socket.error as msg:
            print("ERROR: bind() failed - {}" .format(msg))

        self.s.listen(backlog)

    def fd(self):
        return self.s