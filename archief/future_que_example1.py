import concurrent.futures
import urllib.request
import time
import queue

q = queue.Queue()

URLS = [
    'https://www.youtube.com/watch?v=v2r2riGruPM',
    'https://www.youtube.com/watch?v=yvxMlQrGLkM',
    'https://www.youtube.com/watch?v=nTasT5h0LEg',
    'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
    'https://www.youtube.com/watch?v=84U5NlBOD64',
    'https://www.youtube.com/watch?v=q9MAIwJMc1U',
    'https://www.youtube.com/watch?v=ya6yw7RPjGg',
    'https://www.youtube.com/watch?v=ALZmCy2u0jQ',
    'https://www.youtube.com/watch?v=qVpWpfD27mM',
    'https://www.youtube.com/watch?v=d0FV3_i-6WU+',
    'https://www.youtube.com/watch?v=v2r2riGruPM',
    'https://www.youtube.com/watch?v=yvxMlQrGLkM',
    'https://www.youtube.com/watch?v=nTasT5h0LEg',
    'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
    'https://www.youtube.com/watch?v=84U5NlBOD64',
    'https://www.youtube.com/watch?v=q9MAIwJMc1U',
    'https://www.youtube.com/watch?v=ya6yw7RPjGg',
    'https://www.youtube.com/watch?v=ALZmCy2u0jQ',
    'https://www.youtube.com/watch?v=qVpWpfD27mM',
    'https://www.youtube.com/watch?v=d0FV3_i-6WU+',
    ]


def feed_the_workers(spacing):
    """
    Simulate outside actors sending in work to do, request each url twice
    """
    for url in URLS:
        time.sleep(spacing)
        q.put(url)
    return "DONE FEEDING"


def load_url(url, timeout):
    """ Retrieve a single page and report the URL and contents """
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:

    # start a future for a thread which sends work in through the queue
    future_to_url = {
        executor.submit(feed_the_workers, 0.25): 'FEEDER DONE'}

    while future_to_url:
        # check for status of the futures which are currently working
        done, not_done = concurrent.futures.wait(
            future_to_url, timeout=0.25,
            return_when=concurrent.futures.FIRST_COMPLETED)

        # if there is incoming work, start a new future
        while not q.empty():

            # fetch a url from the queue
            url = q.get()

            # Start the load operation and mark the future with its URL
            future_to_url[executor.submit(load_url, url, 60)] = url

        # process any completed futures
        for future in done:
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                if url == 'FEEDER DONE':
                    print(data)
                else:
                    print('%r page is %d bytes' % (url, len(data)))

            # remove the now completed future
            del future_to_url[future]


# from Queue import Queue
# from threading import Thread

# def do_stuff(q):
#   while True:
#     print q.get()
#     q.task_done()

# q = Queue(maxsize=0)
# num_threads = 10

# for i in range(num_threads):
#   worker = Thread(target=do_stuff, args=(q,))
#   worker.setDaemon(True)
#   worker.start()

# for x in range(100):
#   q.put(x)

# q.join()
# ########
# import threading, queue

# q = queue.Queue()

# def worker():
#     while True:
#         item = q.get()
#         print(f'Working on {item}')
#         print(f'Finished {item}')
#         q.task_done()

# # turn-on the worker thread
# threading.Thread(target=worker, daemon=True).start()

# # send thirty task requests to the worker
# for item in range(30):
#     q.put(item)
# print('All task requests sent\n', end='')

# # block until all tasks are done
# q.join()
# print('All work completed')


'''
Queue class

    recordveld id's in constants voor gemak
    maxrunners = n
    running - started/downloading runners
    init
        queue begint met 1 url
        extend met rest van record velden
            url = 'url'
            status = unknown/started/downloading/ done/finished(?)
            % done - 0
            est time left - False
            future - None
            error - False

'''

# status = unknown/started/downloading/ done/finished(?)
record = [
         'future',
         'status',
         'url',
         'filename',
         'percent_done',
         'est_time_left',
         'error',
        ]


# Test
if __name__ == "__main__":

    print()

#     myqueue = [
#         'https://www.youtube.com/watch?v=v2r2riGruPM',
#         'https://www.youtube.com/watch?v=yvxMlQrGLkM',
#         'https://www.youtube.com/watch?v=nTasT5h0LEg',
#         'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
#         'https://www.youtube.com/watch?v=84U5NlBOD64',
#         'https://www.youtube.com/watch?v=q9MAIwJMc1U',
#         'https://www.youtube.com/watch?v=ya6yw7RPjGg',
#         'https://www.youtube.com/watch?v=ALZmCy2u0jQ',
#         'https://www.youtube.com/watch?v=qVpWpfD27mM',
#         'https://www.youtube.com/watch?v=d0FV3_i-6WU+',
#         ]

#     future_list = FutureList(myqueue)
#     print('Items #: %d' % len(future_list))
#     # print(future_list._items)
#     # print(future_list[3])

#     for item in future_list:
#         print(item)

    # print('While loop')
    # i = 0
    # while i < len(future_list):
    #     print(future_list[i])
    #     i += 1
