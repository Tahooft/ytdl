import threading
import downloader as dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('threader')


def threader(url, urls):

    logger.info('A new url: {} '.format(url))
    threads = []
    urls.append(url)

    while len(urls) > 0:
        url = urls.pop()
        total_urls = len(urls)
        logger.info('URL added: {}'.format(url))
        logger.info('Total urls: {}'.format(total_urls))

        t = threading.Thread(target=dl.downloader, args=[dl.ytdl_opts, url])
        t.start()
        thread = t.getName()
        threads.append(thread)
        total_threads = len(threads)
        logger.info('Latest thread: {}'.format(thread))
        logger.info('Total threads: {}'.format(total_threads))

    t.join()
    logger.info('Done these threads: {}\n'.format(threads))


# Test
if __name__ == "__main__":
    urls = [
        'https://www.youtube.com/watch?v=nTasT5h0LEg',
        'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
        'https://www.youtube.com/watch?v=84U5NlBOD64',
    ]
    # urls = []
    url = 'https://www.youtube.com/watch?v=ya6yw7RPjGg'

    threader(url, urls)
