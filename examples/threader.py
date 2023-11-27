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

    from time import sleep

    urls = [
        'https://www.youtube.com/watch?v=v2r2riGruPM',
        'https://www.youtube.com/watch?v=yvxMlQrGLkM',
        'https://www.youtube.com/watch?v=nTasT5h0LEg',
        'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
        'https://www.youtube.com/watch?v=84U5NlBOD64',
        'https://www.youtube.com/watch?v=q9MAIwJMc1U',
        'https://www.youtube.com/watch?v=ya6yw7RPjGg',
        'https://www.youtube.com/watch?v=ALZmCy2u0jQ',
        'https://www.youtube.com/watch?v=d0FV3_i-6WU+',
    ]
    # urls = []
    url = 'https://www.youtube.com/watch?v=qVpWpfD27mM'

    threader(url, urls)
    sleep(30)
