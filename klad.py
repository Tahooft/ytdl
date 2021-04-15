import logging.config
from concurrent.futures import ThreadPoolExecutor, as_completed

import yaml

import download1 as dl

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


def downloadx(url, urls):
    """
    Create a thread pool and download video's from specified urls
    """

    urls.append(url)

    futures_list = []
    results = {}

    with ThreadPoolExecutor(max_workers=4) as executor:

        for url in urls:
            futures = executor.submit(dl.download1, dl.ydl_opts, url)
            futures_list.append(futures)
            logger.info('[x] Added futures: %s' % futures)
            logger.info('[x] futures_list len: %d ' % len(futures_list))
        logger.info('[x] All futures added\n')

        for future in as_completed(futures_list):
            try:
                result = future.result(timeout=20)
                # results.append(result)
                logger.info('[x] Result: %s ' % result)
                print(futures_list)
                print('[x] Result: %s\n' % result)
            except TimeoutError as terror:
                logger.error('[x] Timeout error!:\n%s' % terror)
            except Exception:
                logger.info('[xe] Exception for future: %s' % future)
                frunning = future.running()
                logger.info('[xe] Future running: %s ' % frunning)
                fdone = future.done()
                logger.info('[xe] Future done: %s ' % fdone)
                results['nope'] = None
            else:
                # frunning = future.running()
                # url als index  (result = url/false)
                fdone = future.done()
                if fdone is False:
                    results['result'] = 'not done'
                else:
                    results[result] = fdone
                results[result] = fdone
                logger.info('[x] Results %s ' % results)

    logger.info('[x] Results returned: %s ' % futures_list)

    print('[x] results verzameld:\n %s' % results)
    return futures_list


# Test
if __name__ == "__main__":

    # from time import sleep

    url = 'https://www.youtube.com/watch?v=4CLzzwDBvlA'   # short file
    # url = 'https://www.youtube.com/watch?v=wXaN2vXEgwg'  # medium file
    # url = 'https://www.youtube.com/watch?v=xwGJYIWhZDM'   # large file

    # 0 urls
    urls = [
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

    results = downloadx(url, urls)
    # sleep(60)
    print()
    logger.info('[x test] Results ..........')
    print()

    # for result in results:
    #     line = result.items
    #     print(f'Result test: {result.items}')
    #     logger.info('[x test]: %s' % key, result)

    print('Returned results:')
    print(results)

    logger.info('[x test] Test done\n\n')
    print('\n......... Test done\n')
    print()
