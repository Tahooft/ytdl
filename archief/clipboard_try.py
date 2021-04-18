import logging.config
import time
from queue import Queue

import pyperclip as clipboard
import yaml

import downloadx as dx
from regulars import isValidURL

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


def main():
    latest = 'go'
    clipboard.copy('go')
    urls = Queue(maxsize=0)

    while clipboard.paste() != 'Stop':

        if clipboard.paste() != latest:
            latest = clipboard.paste()
            logger.info('Latest clipboard item')
            logger.info('clipped: %s' % latest)

            if isValidURL(latest):
                logger.info('Valid url')
                urls.put(latest)
                dx.downloadx(latest, urls)
            else:
                logger.info('Not a valid url')

        time.sleep(5)


# Test
if __name__ == "__main__":
    main()