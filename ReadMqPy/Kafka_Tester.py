from MQ_Tester import MessageQueueTester
from kafka import KafkaProducer


class KafkaTester(MessageQueueTester):
    def test(self):
        try:
            producer = KafkaProducer(bootstrap_servers=self.queue_url)
            producer.close()
            return True
        except Exception:
            return False