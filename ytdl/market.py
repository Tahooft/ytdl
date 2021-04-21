import logging.config
from queue import Queue

import yaml

from producer import ProducerThread, queue, SENTINEL
from consumer import ConsumerThread


with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


ProducerThread().start()
ConsumerThread().start()

