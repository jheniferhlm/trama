from trama.broker import Broker
from trama.consumer import Consumer
from trama.producer import Producer

def test_producer_consumer():
    broker = Broker()
    broker.create_queue("orders")
    producer = Producer(broker)
    consumer = Consumer(broker)
    producer.send("orders", "Pedido 123")
    message = consumer.receive("orders")

    assert message.body == "Pedido 123"