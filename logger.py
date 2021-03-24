import logging


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('logs/test.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

log.addHandler(file_handler)
log.addHandler(stream_handler)

# Test
if __name__ == "__main__":

    log.info(' log deinfobug message')
    log.debug(' log debug message')


# # For possible use
# format = "%(levelname)s:%(name)s:%(asctime)s: %(message)s"

# format = "%(asctime)s: %(message)s"
# logging.basicConfig(format=format, level=logging.INFO,
#                 datefmt="%H:%M:%S")
