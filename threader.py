import threading
import downloader as dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('threader')


def threader(url, urls):

    logger.debug('A new url {} '.format(url))
    urls.append(url)

    while len(urls) > 0:
        url = urls.pop()
        print(len(urls), url)
        logger.debug('url added: {}'.format(url))

        t = threading.Thread(target=dl.downloader, args=[dl.ytdl_opts, url])
        t.start()


# Test
if __name__ == "__main__":
    # urls = [
    #     'https://www.youtube.com/watch?v=nTasT5h0LEg',
    #     'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
    #     'https://www.youtube.com/watch?v=84U5NlBOD64',
    # ]
    urls = []
    url = 'https://www.youtube.com/watch?v=ya6yw7RPjGg'

    threader(url, urls)
