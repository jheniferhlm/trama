import socket

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect(self, address, port):
        self.socket.connect((address, port))
    def send(self, message):
        bitmsg = message.encode('utf-8')
        self.socket.send(bitmsg)
    def receive(self):
        bytesmsg = self.socket.recv(1024)
        strmsg = bytesmsg.decode('utf-8')
        return strmsg