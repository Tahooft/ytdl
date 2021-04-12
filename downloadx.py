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
            running = len(futures_list)

            logger.info('[x] Added futures: %s' % futures)
            logger.info('[x] futures_list len: %d ' % running)
        logger.info('[x] All futures added\n')

        for future in futures_list:
            try:
                result = future.result(timeout=20)
                # results.append(result)
                logger.info('[x] Result: %s ' % result)
                print('[x] Result: %s ' % result)
            except TimeoutError as terror:
                logger.error('[x] Timeout error!:\n%s' % terror)
            except Exception:
                logger.info('[xe] Exception for future: %s' % future)
                frunning = future.running()
                logger.info('[xe] Future running: %s ' % frunning)
                fdone = future.done()
                logger.info('[xe] Future done: %s ' % fdone)
                # excerror = future.exception()
                # logger.error('[x] Exception for future: %s' % excerror)
                if frunning is False:
                    results.append(None)
                else:
                    results.append(result)
            else:
                frunning = future.running()
                logger.info('[x] Future running: %s ' % frunning)
                fdone = future.done()
                logger.info('[x] Future done: %s ' % fdone)
                results.append(result)
        logger.info('[x] Results returned: %s ' % results)
        return results


# Test
if __name__ == "__main__":

    # from time import sleep

    url = 'https://www.youtube.com/watch?v=4CLzzwDBvlA'   # short file
    # url = 'https://www.youtube.com/watch?v=wXaN2vXEgwg'  # medium file
    # url = 'https://www.youtube.com/watch?v=xwGJYIWhZDM'   # large file

    # 0 urls
    urls = []

    results = downloadx(url, urls)

    print()
    logger.info('[x test] Results ..........')

    for result in results:
        print(f'Result test: {result}')
        logger.info('[x test]: %s' % result)

    # sleep(30)
    print('\n......... Test done\n')
    print(results)

    logger.info('[x test] Test done\n\n')
    print()
