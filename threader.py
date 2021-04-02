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
        logger.info(f'URL added: {url}')
        logger.info(f'Total urls: {total_urls}')

        t = threading.Thread(target=dl.downloader, args=[dl.ydl_opts, url])
        t.start()
        thread = t.getName()
        threads.append(thread)
        total_threads = len(threads)
        logger.info(f'Latest thread: {thread}')
        logger.info(f'Total threads: {total_threads}')

    t.join()
    logger.info(f'Done these threads: {threads}\n')


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
