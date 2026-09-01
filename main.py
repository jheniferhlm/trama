from trama.message import Message
from trama.queue import TramaQueue

queue = TramaQueue("orders")

message1 = Message.create("Order 123")
message2 = Message.create("Order 456")

queue.publish(message1)
queue.publish(message2)

print("Messages in queue:", queue.size())

message = queue.consume()

print("Message:")
print("ID:", message.id)
print("Body:", message.body)

print("Messages left:", queue.size())