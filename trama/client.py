import socket

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect(self, address, port):
        self.socket.connect((address, port))