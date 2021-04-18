import logging.config
import time
from queue import Queue
from threading import Thread

import pyperclip as clipboard
import yaml

import download1 as dl
from regulars import isValidURL

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

queue = Queue(maxsize=0)


class ProducerThread(Thread):

    def run(self):
        global queue
        latest = 'go'
        clipboard.copy('go')

        while clipboard.paste() != ' ':

            if clipboard.paste() != latest:
                latest = clipboard.paste()

                if isValidURL(latest):
                    queue.put(latest)
                    print('Produced: %s\n' % latest)

            time.sleep(5)
        print('Trying to stop...')
        queue.put('Stop')
        print('Producer stopped')


class ConsumerThread(Thread):
    """
    Returns list with dicts {url: Downloaded|DownloadError}
    """

    def run(self):

        global queue
        results = Queue(maxsize=0)

        while True:
            url = queue.get()
            if url != 'Stop':
                print('Consumed: %s\n' % url)
                result = dl.download1(dl.ydl_opts, url)
                results.put(result)
                queue.task_done
                print('Done: %s' % url)
                print('Result: %s' % result)
                print('results: %s' % len(results))
            else:
                break
        print('Consumer stopping...')
        queue.join
        print('Consumer stopped')


# Test
if __name__ == "__main__":

    ProducerThread().start()
    ConsumerThread().start()

# https://www.youtube.com/watch?v=qE8PG2mpo58
# https://www.youtube.com/watch?v=v2r2riGruPM
# https://www.youtube.com/watch?v=yvxMlQrGLkM
# https://www.youtube.com/watch?v=gm3dSYAWiUk
# https://www.youtube.com/watch?v=nTasT5h0LEg
# https://www.youtube.com/watch?v=7Ht9jkWXqlU
# https://www.youtube.com/watch?v=84U5NlBOD64
# https://www.youtube.com/watch?v=q9MAIwJMc1U
# https://www.youtube.com/watch?v=ya6yw7RPjGg
# https://www.youtube.com/watch?v=ALZmCy2u0jQ
# https://www.youtube.com/watch?v=qVpWpfD27mM
# https://www.youtube.com/watch?v=d0FV3_i-6WU+
# https://www.youtube.com/watch?v=2KxJ6eTY9bA
