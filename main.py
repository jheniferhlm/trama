import threading
from trama.server import Server
from trama.client import Client

def start_server():
    server = Server()
    connection, address = server.accept()
    print("Cliente conectado:", address)

def start_client():
    client = Client()
    client.connect("127.0.0.1", 5000)
    print("Cliente conectado ao servidor!")

server_thread = threading.Thread(target=start_server)
client_thread = threading.Thread(target=start_client)

server_thread.start()
client_thread.start()
server_thread.join()
client_thread.join()