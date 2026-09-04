from .protocol import Protocol
from .broker import Broker
from .message import Message
import socket

class Server:
    def __init__(self, broker, port=5000):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.broker = broker
        self.port = port
    def start(self):
        self.socket.bind(("127.0.0.1", self.port))
        self.socket.listen()
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
        match command:
            case 'PUBLISH':
                message = Message.create(body)
                return self.broker.publish(queue, message)
            case 'CONSUME':
                return self.broker.consume(queue)
            case _:
                return None