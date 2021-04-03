import threading
import download1 as dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('threader')


def threader(url, urls):

    logger.info('A new url: %s' % url)
    threads = []
    urls.append(url)

    while len(urls) > 0:
        url = urls.pop()
        total_urls = len(urls)
        logger.info('URL added: %s' % url)
        logger.info('Total urls: %d ' % total_urls)

        t = threading.Thread(target=dl.download1, args=[dl.ydl_opts, url])
        t.start()
        thread = t.getName()
        threads.append(thread)
        total_threads = len(threads)
        logger.info('Latest thread: %s' % thread)
        logger.info('Total threads: %s' % total_threads)

    t.join()
    logger.info('Done these threads: %s\n' % threads)


# Test
if __name__ == "__main__":
    urls = [
        'https://www.youtube.com/watch?v=SV6M0MxPGM0',
        'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
        'https://www.youtube.com/watch?v=84U5NlBOD64',
    ]
    # urls = []
    url = 'https://www.youtube.com/watch?v=qVpWpfD27mM'

    threader(url, urls)
