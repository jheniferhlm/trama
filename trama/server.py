from .protocol import Protocol
import socket

class Server:
    def __init__(self, broker):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("127.0.0.1", 5000))
        self.socket.listen()
        self.broker = broker
    def accept(self):
        connection, address = self.socket.accept()
        return connection, address
    def receive(self, connection):
        data = connection.recv(1024)
        strmsg = data.decode('utf-8')
        return strmsg
    def send(self, connection, message):
        bytesmsg = message.encode('utf-8')
        connection.send(bytesmsg)
    def handle(self, message):
        protocol = Protocol()
        command, queue, body = protocol.parse(message)
        return command, queue, body