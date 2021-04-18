import logging.config

from queue import Queue
from threading import Thread

import yaml

import download1 as dl


with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

queue = Queue(maxsize=0)


class ConsumerThread(Thread):
    """
    Create a thread pool and download video's from specified urls\n
    Returns list with dicts {url: Downloaded|DownloadError}
    """

    def run(self):

        global queue

        while True:
            url = queue.get()
            print('Consumed: %s\n' % url)
            result = dl.download1(dl.ydl_opts, url)
            # results.append(result)
            queue.task_done
            print('Done: %s' % url)
            print('Result: %s' % result)
