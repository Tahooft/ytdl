import sys
import concurrent.futures
import random
import time
import math
import queue

MAX_PROCESSES = 4
MAX_THREADS = 5

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def simulateAPICall():
    time.sleep(random.random() / 5)

def randomInt(maximum):
    return int(random.random() * maximum)

def distance(point1, point2):
    simulateAPICall()
    return math.pow(math.pow(point2.x - point1.x, 2) + math.pow(point2.y - point2.x, 2), 0.5)

def thread_worker(point_pair):
    """
    thread worker
    """
    return point_pair, distance(point_pair[0], point_pair[1])

def proc_worker(point_pairs):
    """
    process worker
    """
    q = Queue()
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for point_pair, distance in executor.map(thread_worker, point_pairs):
            p1, p2 = point_pair
            q.put(str(p1.x) + " " + str(p1.y) + ", " + str(p2.x) + ", " + str(p2.y) + ": " + str(distance))
    while not q.empty():
        print(q.get())


class Points(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in xrange(self.n):
            yield(Point(randomInt(10), randomInt(10)), Point(randomInt(10), randomInt(10)))


def start():
    n = 10
    points_per_process = n / MAX_PROCESSES
    # generator is not pickable
    # points = ((Point(randomInt(10), randomInt(10)), Point(randomInt(10), randomInt(10))) for i in xrange(points_per_process))
    points = Points(points_per_process)
    points_lists = [points] * MAX_PROCESSES
    time.sleep(5)

    with concurrent.futures.ProcessPoolExecutor(max_workers=MAX_PROCESSES) as executor:
        for result in executor.map(proc_worker, points_lists):
            pass


def main(argv):
    start()

if __name__ == '__main__':
    main(sys.argv[1:])