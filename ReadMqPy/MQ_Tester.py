
class MessageQueueTester:
    def __init__(self, queue_url):
        self.queue_url = queue_url

    def test(self):
        raise NotImplementedError("Subclasses must implement this method")