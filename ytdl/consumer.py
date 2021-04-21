import logging.config
from queue import Queue
from threading import Thread

import yaml

import download1 as dl

from producer import queue, SENTINEL

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


class ConsumerThread(Thread):
    """
    Returns list with dicts {url: Downloaded|DownloadError}
    """

    def run(self):

        global queue
        results = Queue(maxsize=0)

        while True:
            url = queue.get()
            if url != SENTINEL:
                logger.info('Consumed: %s\n' % url)
                result = dl.download1(url)
                results.put(result)
                queue.task_done

                logger.info('Done: %s' % url)
                logger.info('Result: %s' % result)
                logger.info('results: %s' % results.qsize())
            else:
                break
        logger.info('Consumer stopping...')
        logger.info('Results: %s' % results)
        queue.join
        logger.info('Consumer stopped\n\n')
        print('Consumer stopped')
        