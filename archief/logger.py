import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('tester')


# Test
if __name__ == "__main__":

    logger.debug(' logger debug message')
    logger.info(' logger info message')
    logger.warning(' logger warning message')
    logger.error(' logger error message')
    logger.critical(' logger critical message')


# # For possible use
# format: "%(asctime)s; %(levelname)-8s; [%(process)d]; %(name)-35s;
#      %(funcName)-20s;%(lineno)-4d: %(message)s"
