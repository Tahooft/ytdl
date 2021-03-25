import logging


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

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

log.addHandler(file_handler)
log.addHandler(stream_handler)

# Test
if __name__ == "__main__":

    log.debug(' log debug message')
    log.info(' log info message')
    log.warning(' log warning message')
    log.error(' log error message')
    log.critical(' log critical message')


# # For possible use
# format = "%(levelname)s:%(name)s:%(asctime)s: %(message)s"

# format = "%(asctime)s: %(message)s"
# logging.basicConfig(format=format, level=logging.INFO,
#                 datefmt="%H:%M:%S")
