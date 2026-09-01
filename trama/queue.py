from queue import Queue
from .message import Message

class TramaQueue:
    def __init__(self, name: str):
        self.name = name
        self.messages = Queue()
    def publish(self, message: Message):
        self.messages.put(message)
    def consume(self):
        return self.messages.get()
    def size(self):
        return self.messages.qsize()