from .queue import TramaQueue

class Broker:
    def __init__(self):
        self.queues = {}
    def create_queue(self, name):
        if name not in self.queues:
            self.queues |= {name: TramaQueue(name)}
    def get_queue(self, name):
        return self.queues.get(name)
    def publish(self, name, message):
        queue = self.queues.get(name)
        
        if queue:
            return queue.publish(message)

        return False
    def consume(self, name):
        queue = self.queues.get(name)
        
        if queue:
            return queue.consume()
        
        return None