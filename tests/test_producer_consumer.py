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
    
def test_concurrent_producers():
    broker = Broker()
    broker.create_queue("orders")
    producer1 = Producer(broker)
    producer2 = Producer(broker)
    producer3 = Producer(broker)

    def send_orders(producer, producer_id):
        for i in range(10):
            producer.send("orders", f"Order {producer_id}-{i}")

    thread1 = threading.Thread(target=send_orders, args=(producer1, 1))
    thread2 = threading.Thread(target=send_orders, args=(producer2, 2))
    thread3 = threading.Thread(target=send_orders, args=(producer3, 3))

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

    assert broker.get_queue("orders").size() == 30