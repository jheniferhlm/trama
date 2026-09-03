from trama.protocol import Protocol

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