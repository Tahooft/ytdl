import threading
import downloader as dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('klad')


def threader():
    urls = [
        'https://www.youtube.com/watch?v=nTasT5h0LEg',
        'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
        'https://www.youtube.com/watch?v=84U5NlBOD64',
    ]

    while len(urls) > 0:
        url = urls.pop()
        print(len(urls), url)

        t = threading.Thread(target=dl.downloader, args=[dl.ytdl_opts, url])
        t.start()


# Test
if __name__ == "__main__":
    threader()
