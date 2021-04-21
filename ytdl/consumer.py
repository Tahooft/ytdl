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


# long_list = [
#     'https://www.youtube.com/watch?v=qE8PG2mpo58',
#     'https://www.youtube.com/watch?v=v2r2riGruPM',
#     'https://www.youtube.com/watch?v=yvxMlQrGLkM',
#     'https://www.youtube.com/watch?v=gm3dSYAWiUk',
#     'https://www.youtube.com/watch?v=nTasT5h0LEg',
#     'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
#     'https://www.youtube.com/watch?v=84U5NlBOD64',
#     'https://www.youtube.com/watch?v=q9MAIwJMc1U',
#     'https://www.youtube.com/watch?v=ya6yw7RPjGg',
#     'https://www.youtube.com/watch?v=ALZmCy2u0jQ',
#     'https://www.youtube.com/watch?v=qVpWpfD27mM',
#     'https://www.youtube.com/watch?v=d0FV3_i-6WU+',
#     'https://www.youtube.com/watch?v=2KxJ6eTY9bA',
#     SENTINEL
# ]

short_list = [

    'https://www.youtube.com/watch?v=d0FV3_i-6WU+',
    'https://www.youtube.com/watch?v=2KxJ6eTY9bA',
    SENTINEL
]

print(queue.qsize)
print(SENTINEL)
for url in short_list:
    queue.put(url)

print(queue.qsize())

result = ConsumerThread().start()
print(result)
