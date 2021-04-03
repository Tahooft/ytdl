from concurrent.futures import ThreadPoolExecutor
import downloader as dl
import logging.config
import yaml
from time import sleep


with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('download_all')


def download_all(url, urls):
    """
    Create a thread pool and download video's from specified urls
    """

    urls.append(url)

    futures_list = []
    results = []

    with ThreadPoolExecutor(max_workers=4) as executor:
        for url in urls:
            futures = executor.submit(dl.downloader, dl.ydl_opts, url)
            futures_list.append(futures)
            logger.debug('futures_list: %s ' % futures_list)

        for future in futures_list:
            try:
                result = future.result(timeout=20)
                results.append(result)
                logger.debug('result: %s ' % result)

            except Exception:
                results.append(None)

    return results


if __name__ == "__main__":

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

    results = download_all(url, urls)
    for result in results:
        print(f'Result: {result}')
    sleep(60)
    print('Done\n')
