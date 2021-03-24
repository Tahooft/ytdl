import logger
import time
import pyperclip as clipboard
from regulars import isValidURL
import downloader as dl


def looper():
    latest = 'go'
    clipboard.copy('go')

    while clipboard.paste() != 'Stop':

        if clipboard.paste() != latest:
            latest = clipboard.paste()
            logger.log.info('Latest clipboard item')
            logger.log.info('clipped: {}'.format(latest))

            if isValidURL(latest):
                logger.log.info('Valid url')
                dl.downloader(dl.ytdl_opts, latest)
            else:
                logger.log.debug('Not a valid url')

        time.sleep(5)


# Test
if __name__ == "__main__":
    looper()

# # For possible use
# format = "%(levelname)s:%(name)s:%(asctime)s: %(message)s"

# format = "%(asctime)s: %(message)s"
# logging.basicConfig(format=format, level=logging.INFO,
#                 datefmt="%H:%M:%S")
