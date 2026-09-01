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
    def is_empty():
        return self.messages.empty()
    def clear():
        while not self.messages.empty():
            self.messages.get()
    def peek(self):
        if self.messages.empty():
            return None
    
        return self.messages.queue[0]
    def try_consume(self):
        if self.messages.empty():
            return None
        
        return self.messages.get(block=False)