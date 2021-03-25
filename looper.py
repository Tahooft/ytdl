import time
import pyperclip as clipboard
from regulars import isValidURL
import downloader as dl
import logging
import logging.config

logging.config.fileConfig(fname='log.conf')
logger = logging.getLogger('dev')


def looper():
    latest = 'go'
    clipboard.copy('go')

    while clipboard.paste() != 'Stop':

        if clipboard.paste() != latest:
            latest = clipboard.paste()
            logger.info('Latest clipboard item')
            logger.info('clipped: {}'.format(latest))

            if isValidURL(latest):
                logger.info('Valid url')
                dl.downloader(dl.ytdl_opts, latest)
            else:
                logger.debug('Not a valid url')

        time.sleep(5)


# Test
if __name__ == "__main__":
    looper()
