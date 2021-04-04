from concurrent.futures import ThreadPoolExecutor
import download1 as dl
import logging.config
import yaml


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
    results = []

    with ThreadPoolExecutor(max_workers=4) as executor:
        for url in urls:
            futures = executor.submit(dl.download1, dl.ydl_opts, url)
            futures_list.append(futures)
            logger.debug('futures_list len: %s ' % len(futures_list))

        for future in futures_list:
            try:
                result = future.result(timeout=20)
                results.append(result)
                logger.debug('result: %s ' % result)

            except TimeoutError as terror:
                logger.error('\nTimeout error!:\n%s\n' % terror)

            except Exception as e:
                results.append(None)
                logger.error('\nDownloadx error!:\n%s\n' % e)

            else:
                fdone = future.done
                logger.debug('Future done: %s ' % fdone)

    return results


# Test
if __name__ == "__main__":

    from time import sleep

    url = 'https://www.youtube.com/watch?v=qVpWpfD27mM'

    urls = [
        'https://www.youtube.com/watch?v=v2r2riGruPM',
        'https://www.youtube.com/watch?v=yvxMlQrGLkM',
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
    for result in results:
        print(f'Result: {result}')
        logger.info('Result: %s' % result)

    print('Done\n')
    logger.debug('Done\n')
    sleep(30)
