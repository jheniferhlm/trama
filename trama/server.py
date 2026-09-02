import socket

class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("127.0.0.1", 5000))
        self.socket.listen()
    def accept(self):
        connection, address = self.socket.accept()
        return connection, address