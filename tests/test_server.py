from trama.broker import Broker
from trama.server import Server

def test_handle_publish():
    broker = Broker()
    broker.create_queue("orders")
    server = Server(broker)
    server.handle("PUBLISH orders Order 123")
    message = broker.consume("orders")

    assert message.body == "Order 123"
    
def test_server_has_broker():
    broker = Broker()
    server = Server(broker)

    assert server.broker == broker