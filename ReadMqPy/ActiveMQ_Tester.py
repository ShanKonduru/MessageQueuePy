from MQ_Tester import MessageQueueTester
import stomp

class ActiveMQTester(MessageQueueTester):
    def test(self):
        try:
            conn = stomp.Connection([(self.queue_url, 61613)])
            conn.start()
            conn.connect(wait=True)
            conn.disconnect()
            return True
        except Exception:
            return False