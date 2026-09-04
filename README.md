# Trama

A lightweight message broker built from scratch exploring queues, concurrency, TCP sockets, and distributed systems concepts.

## About

Trama is a learning-focused message broker developed from scratch using vanilla Python.
The project aims to explore how message brokers work internally, from basic queues to network communication, concurrency, message delivery, FIFO, and distributed systems concepts.

## Architecture

```text
Producer
   │
   ▼
 Broker
   │
   ▼
 Queue
   │
   ▼
Consumer
```

The TCP layer allows clients and servers to communicate like this:

```text
Client ────── TCP ──────> Server
          messages
```

## Structure

```text
trama/
├── trama/
│   ├── __init__.py
│   ├── message.py
│   ├── queue.py
│   ├── broker.py
│   ├── producer.py
│   ├── consumer.py
│   ├── server.py
│   ├── protocol.py
│   └── client.py
│
├── tests/
│   ├── test_queue.py
│   ├── test_broker.py
│   ├── test_protocol.py
│   └── test_producer_consumer.py
│
└── main.py
```

## Roadmap

* [x] Message model
* [x] In-memory queue
* [x] Broker
* [x] Producer / Consumer
* [x] Concurrent producers
* [x] Concurrent consumers
* [x] TCP server
* [x] TCP client
* [x] Basic message transmission
* [x] Communication protocol
* [x] ACKs
* [ ] Multiple client connections
* [ ] Broker + TCP integration
* [ ] Message retries
* [ ] Dead-letter queue
* [ ] Message persistence
* [ ] Logging and metrics
* [ ] Monitoring dashboard