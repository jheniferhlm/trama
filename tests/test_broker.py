from trama.broker import Broker

def test_broker_starts_without_queues():
    broker = Broker()

    assert len(broker.queues) == 0

def test_create_queue():
    broker = Broker()
    broker.create_queue("orders")

    assert "orders" in broker.queues
    
def test_create_existing_queue_does_not_create_another():
    broker = Broker()
    broker.create_queue("orders")
    first_queue = broker.queues["orders"]
    broker.create_queue("orders")
    second_queue = broker.queues["orders"]

    assert first_queue is second_queue
    assert len(broker.queues) == 1
    
def test_get_queue():
    broker = Broker()
    broker.create_queue("orders")
    queue = broker.get_queue("orders")

    assert queue is not None
    assert queue.name == "orders"
    
def test_get_nonexistent_queue():
    broker = Broker()
    queue = broker.get_queue("orders")

    assert queue is None