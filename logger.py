import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


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
