import re
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('regulars')


def isValidURL(str):
    '''
    Validate url using regular expression\n
    Return True if str is valid url otherwise False
    '''

    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # Test for empty string
    # if str is None:
    #     return False

    return True if (re.search(p, str)) else False


# Test
if __name__ == "__main__":

    url = "https://www.geeksforgeeks.org"

    if(isValidURL(url) is True):
        logger.info('Yes')
    else:
        logger.info('no')
