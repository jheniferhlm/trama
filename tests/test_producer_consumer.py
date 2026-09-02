from trama.broker import Broker
from trama.consumer import Consumer
from trama.producer import Producer
import threading

def test_producer_consumer():
    broker = Broker()
    broker.create_queue("orders")
    producer = Producer(broker)
    consumer = Consumer(broker)
    producer.send("orders", "Order 123")
    message = consumer.receive("orders")

    assert message.body == "Order 123"