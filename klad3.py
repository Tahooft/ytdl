
import logging
import logging.config

logging.config.fileConfig(fname='log.conf')
logger = logging.getLogger('dev')


# Test
if __name__ == "__main__":

    logger.debug(' logger debug message')
    logger.info(' logger info message')
    logger.warning(' logger warning message')
    logger.error(' logger error message')
    logger.critical(' logger critical message')
