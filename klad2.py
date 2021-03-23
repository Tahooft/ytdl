import threading
import time
import youtu

start = time.perf_counter()


urls = [
    'https://www.youtube.com/watch?v=nTasT5h0LEg',
    'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
    'https://www.youtube.com/watch?v=84U5NlBOD64',
]


threads = []

for url in urls:
    t = threading.Thread(target=youtu.downloader, args=[youtu.ytdl_opts, url])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
