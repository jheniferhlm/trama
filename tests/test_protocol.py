from trama.protocol import Protocol
from trama.broker import Broker
from trama.message import Message
import pytest

def test_parse_publish():
    protocol = Protocol()
    command, queue, body = protocol.parse("PUBLISH orders Order 123")

    assert command == "PUBLISH"
    assert queue == "orders"
    assert body == "Order 123"


def test_parse_consume():
    protocol = Protocol()
    command, queue, body = protocol.parse("CONSUME orders")

    assert command == "CONSUME"
    assert queue == "orders"
    assert body == ""
    
def test_parse_invalid():
    protocol = Protocol()
    with pytest.raises(ValueError):
        command, queue, body = protocol.parse("DELETE orders")
        
def test_parse_publish_without_body():
    protocol = Protocol()
    with pytest.raises(ValueError):
        protocol.parse("PUBLISH orders")


def test_parse_consume_without_queue():
    protocol = Protocol()
    with pytest.raises(ValueError):
        protocol.parse("CONSUME")
        
def test_parse_publish_with_empty_message():
    protocol = Protocol()
    with pytest.raises(ValueError):
        protocol.parse("PUBLISH orders  ")
        
def test_parse_publish_empty_body():
    protocol = Protocol()
    with pytest.raises(ValueError):
        protocol.parse("PUBLISH orders ")
        
def test_publish_command():
    protocol = Protocol()
    broker = Broker()
    command, queue, body = protocol.parse("PUBLISH orders Order 123")
    
    broker.create_queue(queue)
    message = Message.create(body)
    broker.publish(queue, message)
    received = broker.consume(queue)
    
    assert command == "PUBLISH"
    assert queue == "orders"
    assert body == "Order 123"
    assert received.body == "Order 123"