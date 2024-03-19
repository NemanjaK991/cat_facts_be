import json
import logging


class ConfReader:

    def __init__(self, conf_file_path):
        try:
            with open(conf_file_path, 'r') as conf:
                conf_json = json.load(conf)

            self.__dict__.update(conf_json)

        except FileNotFoundError:
            logging.error('Logging: The config file is not found')

    def get_base_url(self):
        if hasattr(self, 'base_url'):
            return self.base_url
