from .queue import TramaQueue

class Broker:
    def __init__(self):
        self.queues = {}
    def create_queue(self, name):
        if name not in self.queues:
            self.queues |= {name: TramaQueue(name)}
    def get_queue(self, name):
        return self.queues.get(name)