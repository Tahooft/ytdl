import random
import time
from threading import Thread

from Queue import Queue

queue = Queue(10)


class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print("Produced %s" % num)
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print("Consumed %s" % num)
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()
