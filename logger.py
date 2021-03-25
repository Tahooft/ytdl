import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

basicformat = '%(levelname)s:%(name)s:%(message)s'
format = '%(asctime)s:' + basicformat

formatter = logging.Formatter(basicformat)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

formatter = logging.Formatter(format)
file_handler = logging.FileHandler('logs/test.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Test
if __name__ == "__main__":

    logger.debug(' logger debug message')
    logger.info(' logger info message')
    logger.warning(' logger warning message')
    logger.error(' logger error message')
    logger.critical(' logger critical message')


# # For possible use
# format = "%(levelname)s:%(name)s:%(asctime)s: %(message)s"

# format = "%(asctime)s: %(message)s"
# logging.basicConfig(format=format, level=logging.INFO,
#                 datefmt="%H:%M:%S")
