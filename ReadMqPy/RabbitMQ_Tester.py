from MQ_Tester import MessageQueueTester
import pika

class RabbitMQTester(MessageQueueTester):
    def test(self):
        try:
            connection = pika.BlockingConnection(pika.URLParameters(self.queue_url))
            connection.close()
            return True
        except Exception:
            return False
        