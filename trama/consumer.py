from .broker import Broker
from .message import Message

class Consumer:
    def __init__(self, broker: Broker):
        self.broker = broker
    def receive(self, queue_name):
        return self.broker.consume(queue_name)