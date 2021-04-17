import logging.config
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

import yaml

import download1 as dl

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


def downloadx(urls):
    """
    Create a thread pool and download video's from specified urls\n
    Returns list with dicts {url: Downloaded|DownloadError}
    """

    q = Queue(maxsize=0)
    results = []

    with ThreadPoolExecutor(max_workers=4) as executor:

        while not urls.empty():
            url = urls.get()
            futures = executor.submit(dl.download1, dl.ydl_opts, url)
            q.put(futures)
            logger.info('[x] Added futures: %s' % futures)
        logger.info('[x] All futures added\n')

        while not q.empty():
            future = q.get()
            try:
                result = future.result(timeout=30)
            except TimeoutError as terror:
                logger.error('[x] TimeoutError:\n%s' % terror)
            except UnboundLocalError as unbound:
                print('Unbound: %s ! ' % unbound)
                results.append('Unbound')
                results.append(result)
                logger.info('[xe] UnboundLocalError: %s' % unbound)
            except Exception:
                results.append('Exception')
                results.append(result)
                logger.info('[xe] Exception for future: %s' % future)
            else:
                # frunning = future.running()
                if future.done() is True:
                    results.append(result)
                    logger.info('[x] Results %s ' % results)
        # logger.info('[x] Final results q: %s\n' % q)
        logger.info('[x] Final results: %s\n' % results)

    return results


# Test
if __name__ == "__main__":

    urls = Queue(maxsize=0)

    # from time import sleep

    # url = 'https://www.youtube.com/watch?v=4CLzzwDBvlA'   # short file
    # url = 'https://www.youtube.com/watch?v=wXaN2vXEgwg'  # medium file
    # url = 'https://www.youtube.com/watch?v=xwGJYIWhZDM'   # large file

    # 13 urls (+1 voor url)
    test_urls = [
        'https://www.youtube.com/watch?v=2KxJ6eTY9bA',
        'https://www.youtube.com/watch?v=qE8PG2mpo58',
        'https://www.youtube.com/watch?v=v2r2riGruPM',
        'https://www.youtube.com/watch?v=yvxMlQrGLkM',
        'https://www.youtube.com/watch?v=gm3dSYAWiUk',
        'https://www.youtube.com/watch?v=nTasT5h0LEg',
        'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
        'https://www.youtube.com/watch?v=84U5NlBOD64',
        'https://www.youtube.com/watch?v=q9MAIwJMc1U',
        'https://www.youtube.com/watch?v=ya6yw7RPjGg',
        'https://www.youtube.com/watch?v=ALZmCy2u0jQ',
        'https://www.youtube.com/watch?v=qVpWpfD27mM',
        'https://www.youtube.com/watch?v=d0FV3_i-6WU+',
    ]

    for url in test_urls:
        urls.put(url)

    results = downloadx(urls)
    # sleep(60)
    print()
    logger.info('[x test] Results ..........')
    print()

    for result in results:
        print('x test: %s' % result)
        logger.info('[x test]: %s' % result)

    logger.info('[x test] Test done\n\n')
    print('\n......... Test done\n')
    print()
