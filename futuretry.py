import concurrent.futures
import downloader as dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('futuretry')


URLS = ['https://www.youtube.com/watch?v=nTasT5h0LEg',
        'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
        'https://www.youtube.com/watch?v=84U5NlBOD64',
        'https://www.youtube.com/watch?v=ya6yw7RPjGg',
        'https://www.youtube.com/watch?v=ALZmCy2u0jQ',
        'https://www.youtube.com/watch?v=qVpWpfD27mM',
        'https://www.youtube.com/watch?v=d0FV3_i-6WU+']


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(dl.downloader, dl.ytdl_opts, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
            logger.exception('%r generated an exception: %s' % (url, exc))
        else:
            print('%r has %s' % (url, data))
            logger.info('Downloader %r returns: %s' % (url, data))

        wait()
