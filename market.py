import logging.config
from queue import Queue

import yaml

from consumer import ConsumerThread
from producer import ProducerThread

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

queue = Queue(maxsize=0)

ProducerThread().start()
ConsumerThread().start()


# Test
# if __name__ == "__main__":

#     ProducerThread().start()
#     ConsumerThread().start()

# https://www.youtube.com/watch?v=qE8PG2mpo58
# https://www.youtube.com/watch?v=v2r2riGruPM
# https://www.youtube.com/watch?v=yvxMlQrGLkM
# https://www.youtube.com/watch?v=gm3dSYAWiUk
# https://www.youtube.com/watch?v=nTasT5h0LEg
# https://www.youtube.com/watch?v=7Ht9jkWXqlU
# https://www.youtube.com/watch?v=84U5NlBOD64
# https://www.youtube.com/watch?v=q9MAIwJMc1U
# https://www.youtube.com/watch?v=ya6yw7RPjGg
# https://www.youtube.com/watch?v=ALZmCy2u0jQ
# https://www.youtube.com/watch?v=qVpWpfD27mM
# https://www.youtube.com/watch?v=d0FV3_i-6WU+
# https://www.youtube.com/watch?v=2KxJ6eTY9bA
