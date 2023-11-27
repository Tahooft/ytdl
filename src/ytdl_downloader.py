# i want a python class that takes an url as parameter and then start yt-dlp to download the file stated in that url.
# i want to be able to set all the options for yt-dlp.
# i want to keep track of the progress of the download
# if the download has succeeded it returns the url otherwise the boolean FALSE


import os
import sys
import threading
from queue import LifoQueue, Empty
from typing import List
import asyncio
from functools import partial

from yt_dlp import YoutubeDL


class YTDLDownloader:
    def __init__(self):
        self.queue = LifoQueue()
        self.thread = None
        self.future = None

    def download(self, url: str, options: dict) -> str:
        yt_dlp_hook_partial = partial(self.yt_dlp_hook, self.queue)
        ydl_opts = {
            'quiet': True,
            'noprogress': True,
            **options,
            'progress_hooks': [yt_dlp_hook_partial]
        }
        with YoutubeDL(ydl_opts) as ydl:
            self.future = ydl.download([url])
        self.thread = threading.Thread(
            target=self.loop_in_thread, args=[self.future])
        self.thread.start()
        while not self.future.done():
            try:
                data = self.queue.get_nowait()
                if data['status'] == 'downloading':
                    print(f"Status: {data['status']} | Downloaded {data['downloaded_bytes']/data['total_bytes']:.0%} "
                          f"{data['downloaded_bytes']}/{data['total_bytes']} bytes")
                elif data['status'] == 'finished':
                    return data['filename']
            except Empty:
                pass
        return False

    @staticmethod
    def yt_dlp_hook(queue: LifoQueue, download):
        queue.put(download)

    @staticmethod
    def loop_in_thread(future):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(future)


# The YTDLDownloader class has a download method that takes a URL and options as input and downloads the file using yt-dlp.
# It returns the filename on success and boolean False on failure. The yt_dlp_hook method is used to track the progress of the download. T
# he loop_in_thread method is used to run the event loop in a separate thread.

# Here’s an example usage:

# url = 'https://www.example.com/index.html'
# options = {
#     'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
#     'outtmpl': os.path.join(os.getcwd(), '%(title)s.%(ext)s'),
#     'noplaylist': True,
#     'nooverwrites': True,
#     'continuedl': True,
#     'quiet': True,
#     'no_warnings': True,
#     'restrictfilenames': True,
#     'ignoreerrors': True,
#     'socket_timeout': 5,
#     'retries': 3,
#     'fragment_retries': 3,
#     'skip_unavailable_fragments': True,
#     'external_downloader': 'aria2c',
#     'external_downloader_args': ['-x', '16', '-s', '16', '-k', '1M'],
#     'postprocessors': [{
#         'key': 'FFmpegVideoConvertor',
#         'preferedformat': 'mp4'
#     }]
# }

# ytdl_downloader = YTDLDownloader()
# filename = ytdl_downloader.download(url, options)
# if filename:
#     print(f"Download succeeded: {filename}")
# else:
#     print("Download failed.")

# The download method takes a URL and options as input and downloads the file using yt-dlp.
# The options parameter is a dictionary that contains all the options for yt-dlp.
# The filename variable contains the filename on success and boolean False on failure.
# You can use the filename variable to check if the download succeeded or failed.
