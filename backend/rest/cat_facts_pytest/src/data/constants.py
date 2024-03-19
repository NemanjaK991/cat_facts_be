import os
from enum import Enum

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(DATA_DIR, '.env')
CONF_FILE_PATH = os.path.join(DATA_DIR, 'config.json')


class Uri(Enum):
    FACTS = '/facts'
    RANDOM = '/random'



