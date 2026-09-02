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
    
def test_concurrent_consumers():
    broker = Broker()
    broker.create_queue("orders")
    producer = Producer(broker)
    
    for i in range(30):
        producer.send("orders", f"Order {i}")
    
    consumer1 = Consumer(broker)
    consumer2 = Consumer(broker)
    consumer3 = Consumer(broker)
    received = []
    
    def read_orders(consumer, consumer_id):
        for i in range(10):
            message = consumer.receive("orders")
            received.append(message)
            
    thread1 = threading.Thread(target=read_orders, args=(consumer1, 1))
    thread2 = threading.Thread(target=read_orders, args=(consumer2, 2))
    thread3 = threading.Thread(target=read_orders, args=(consumer3, 3))

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
            
    assert len(received) == 30
    assert broker.get_queue("orders").size() == 0