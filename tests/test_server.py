from trama.broker import Broker
from trama.server import Server
import socket

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
    
def test_server_process():
    broker = Broker()
    broker.create_queue("orders")
    server = Server(broker)
    socket1, socket2 = socket.socketpair()
    socket1.send("PUBLISH orders Order 123".encode('utf-8'))
    server.process(socket2)
    message = broker.consume("orders")
    socket1.close()
    socket2.close()

    assert message.body == "Order 123"
    
def test_server_process_sends_ack():
    broker = Broker()
    broker.create_queue("orders")
    server = Server(broker)
    socket1, socket2 = socket.socketpair()
    socket1.send("PUBLISH orders Order 123".encode("utf-8"))
    server.process(socket2)
    response = socket1.recv(1024).decode("utf-8")

    assert response == "ACK"