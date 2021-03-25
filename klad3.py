
import logging
import logging.config

logging.config.fileConfig(fname='log.conf')

logger = logging.getLogger('dev')
logger.info('This is an information message')
