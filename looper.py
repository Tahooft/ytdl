import time
import pyperclip as clipboard
from regulars import isValidURL
import downloader as dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('looper')


def looper():
    latest = 'go'
    clipboard.copy('go')

    while clipboard.paste() != 'Stop':

        if clipboard.paste() != latest:
            latest = clipboard.paste()
            logger.info('Latest clipboard item')
            logger.info(f'clipped: {latest}')

            if isValidURL(latest):
                logger.info('Valid url')
                dl.downloader(dl.ytdl_opts, latest)
            else:
                logger.debug('Not a valid url')

        time.sleep(5)


# Test
if __name__ == "__main__":
    looper()
