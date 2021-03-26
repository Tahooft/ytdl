import threading
import time
import downloader as dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('thread_them')

start = time.perf_counter()


urls = [
    'https://www.youtube.com/watch?v=nTasT5h0LEg',
    'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
    'https://www.youtube.com/watch?v=84U5NlBOD64',
]


threads = []

for url in urls:
    t = threading.Thread(target=dl.downloader, args=[dl.ytdl_opts, url])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
logger.debug(f'Finished in {round(finish-start, 2)} second(s)')
