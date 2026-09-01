from trama.message import Message
from trama.queue import TramaQueue

def test_queue_starts_empty():
    queue = TramaQueue("orders")
    
    assert queue.size() == 0
    
def test_publish_adds_message_to_queue():
    queue = TramaQueue("orders")
    message = Message.create("Order 123")
    queue.publish(message)
    
    assert queue.size() == 1
    
def test_consume_returns_message():
    queue = TramaQueue("orders")
    message = Message.create("Order 123")
    queue.publish(message)
    result = queue.consume()
    
    assert result == message
    
def test_queue_is_fifo():
    queue = TramaQueue("orders")

    message1 = Message.create("Order 123")
    message2 = Message.create("Order 456")
    message3 = Message.create("Order 789")

    queue.publish(message1)
    queue.publish(message2)
    queue.publish(message3)

    assert queue.consume() == message1
    assert queue.consume() == message2
    assert queue.consume() == message3
    
def test_try_consume_empty_queue():
    queue = TramaQueue("orders")
    result = queue.try_consume()

    assert result is None
    
def test_try_consume_returns_message():
    queue = TramaQueue("orders")
    message = Message.create("Pedido 123")
    queue.publish(message)
    result = queue.try_consume()

    assert result == message
    assert queue.size() == 0