import logging.config
import time
from queue import Queue
from threading import Thread

import pyperclip as clipboard
import yaml

from regulars import isValidURL

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

queue = Queue(maxsize=0)
SENTINEL = 'Stop'


class ProducerThread(Thread):
    """ Watch the clipboard for valid urls to put them in the queue """

    def run(self):
        global queue
        latest = 'go'
        clipboard.copy('go')

        while clipboard.paste() != SENTINEL:

            if clipboard.paste() != latest:
                latest = clipboard.paste()

                if isValidURL(latest):
                    queue.put(latest)
                    logger.info('Produced: %s\n' % latest)

            time.sleep(5)

        logger.info('Trying to stop...')
        queue.join()
        logger.info('Producer stopped')
