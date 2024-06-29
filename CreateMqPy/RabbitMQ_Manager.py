import pika
import json

class RabbitMQManager:
    def __init__(self, host='localhost', port=5672, username='admin', password='admin'):
        self.host = host
        self.port = port
        self.credentials = pika.PlainCredentials(username, password)
        self.connection = None
        self.channel = None

    def connect(self):
        try:
            print(f"Connecting to RabbitMQ at {self.host}:{self.port} with username '{self.credentials.username}'")
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=self.host, port=self.port, credentials=self.credentials))
            self.channel = self.connection.channel()
            print("Connected to RabbitMQ")
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Failed to connect to RabbitMQ: {e}")
            raise

    def declare_queue(self, queue_name):
        if self.channel:
            self.channel.queue_declare(queue=queue_name)
            print(f"Declared queue: {queue_name}")
        else:
            print("Connection is not established. Cannot declare queue.")

    def send_message(self, queue_name, message):
        if self.channel:
            self.channel.basic_publish(exchange='',
                                       routing_key=queue_name,
                                       body=message)
            print(f"Sent message to {queue_name}: {message}")
        else:
            print("Connection is not established. Cannot send message.")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
        else:
            print("Connection is not established. Cannot close connection.")
