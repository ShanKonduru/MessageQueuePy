import configparser

class ConfigReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get_queues(self):
        queues = []
        for section in self.config.sections():
            queue_url = self.config[section]['url']
            queue_type = self.config[section]['type']
            queues.append((section, queue_url, queue_type))
        return queues