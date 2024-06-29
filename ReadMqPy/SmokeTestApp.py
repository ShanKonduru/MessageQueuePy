from datetime import datetime

from Config_Reader import ConfigReader 
from RabbitMQ_Tester import RabbitMQTester
from Kafka_Tester import KafkaTester
from ActiveMQ_Tester import ActiveMQTester
from Report_Generator import ReportGenerator

def get_tester(queue_type, queue_url):
    if queue_type == 'RabbitMQ':
        return RabbitMQTester(queue_url)
    elif queue_type == 'Kafka':
        return KafkaTester(queue_url)
    elif queue_type == 'ActiveMQ':
        return ActiveMQTester(queue_url)
    else:
        raise ValueError(f"Unsupported queue type: {queue_type}")

class SmokeTestApp:
    def __init__(self, config_path):
        self.config_reader = ConfigReader(config_path)
        self.results = []

    def run_tests(self):
        queues = self.config_reader.get_queues()
        for name, url, queue_type in queues:
            tester = get_tester(queue_type, url)
            result = tester.test()
            self.results.append((name, url, queue_type, result))

    def generate_report(self, report_path):
        report_generator = ReportGenerator(self.results)
        report_generator.generate_html(report_path)

def main(config_path, report_path):
    app = SmokeTestApp(config_path)
    app.run_tests()
    app.generate_report(report_path)

if __name__ == "__main__":
    config_path = 'queues.ini'
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = f'report_{current_time}.html'
    main(config_path, report_path)