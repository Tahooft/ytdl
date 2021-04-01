from concurrent.futures import ThreadPoolExecutor, as_completed
# from concurrent.futures import ThreadPoolExecutor, wait

from time import sleep
from random import randint
from timeit import timeit as timeit


@timeit
def return_after_5_secs(num):
    sleep(randint(1, 5))
    print(f'Return of {num}')
    # return True


pool = ThreadPoolExecutor(5)
futures = []
for x in range(5):
    futures.append(pool.submit(return_after_5_secs, x))

for x in as_completed(futures):
    print(x.result())

# print(wait(futures))
