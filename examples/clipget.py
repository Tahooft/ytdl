import pyperclip as clipboard
from regulars import isValidURL
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


def clipget():

    if clipboard.waitForNewPaste():
        latest = clipboard.paste()
        logger.info('Latest clipboard item')
        logger.info('clipget: %s' % latest)

        if isValidURL(latest):
            logger.info(latest)
            result = latest
        else:
            logger.info('Not a valid url')
            result = 'Not a valid url'
    return result


# Test
if __name__ == "__main__":

    result = clipget()
    logger.info('[d1 test] End of test')
    print('Done: %s \n ' % result)


# sample url: https://www.youtube.com/watch?v=DJdqMs6OUyI&list=TLPQMjIxMTIwMjOWwvRVfIDwuQ&index=2
# waitForNewPaste()
#     if clipboard.paste() != 'Stop':

# pyperclip.copy()  to fill the clipboard
