from .broker import Broker
from .message import Message

class Producer:
    def __init__(self, broker: Broker):
        self.broker = broker
    def send(self, queue_name, body):
        message = Message.create(body)
        self.broker.publish(queue_name, message)