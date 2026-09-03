from trama.protocol import Protocol
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