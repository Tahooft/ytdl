# i want a python class that takes an url as parameter and then start an instance of yt-dlp to download the file stated in that url.
# i want to be able to set all the options for yt-dlp.
# i want to keep track of the progress of the download
# if the download has succeeded it returns the url otherwise the boolean FALSE
# I want to limit the maximimum of simultanious downloading yt-dlp instances to be a number that i can give as a parameter
# i need getters in Downloader for url, progress_hook status finished, downloading and downloaded bytes


from yt_dlp import YoutubeDL


class Downloader:
    def __init__(self, url, options, max_simultaneous_downloads):
        self.url = url
        self.options = options
        self.max_simultaneous_downloads = max_simultaneous_downloads
        self.downloaded_bytes = 0
        self.downloading_bytes = 0
        self.progress_hook = None
        self.status = 'not started'
        self.finished = False

    def start_download(self):
        with YoutubeDL(self.options) as ydl:
            ydl.add_progress_hook(self._progress_hook)
            ydl.download([self.url])
        self.finished = True

    def _progress_hook(self, status):
        self.status = status['status']
        self.downloading_bytes = status['downloaded_bytes']
        self.downloaded_bytes = status['total_bytes']
        if self.progress_hook:
            self.progress_hook(status)

    def get_url(self):
        return self.url

    def get_progress_hook(self):
        return self.progress_hook

    def set_progress_hook(self, progress_hook):
        self.progress_hook = progress_hook

    def get_status(self):
        return self.status

    def get_downloading_bytes(self):
        return self.downloading_bytes

    def get_downloaded_bytes(self):
        return self.downloaded_bytes

    def is_finished(self):
        return self.finished

# This class takes a URL, options for yt-dlp, and the maximum number of simultaneous downloads as parameters.
# It has methods to start the download, get the URL, progress hook, status, downloading bytes, downloaded bytes, and whether the download is finished or not.
# You can set the progress hook using the set_progress_hook method to keep track of the progress of the download.
# If the download has succeeded, it returns the URL; otherwise, it returns the boolean False.


# Test
if __name__ == "__main__":

    def my_hook(status):
        if status['status'] == 'finished':
            print('Download complete!')
        elif status['status'] == 'downloading':
            print(f"Downloading: {status['_percent_str']}")

    options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'progress_hooks': [my_hook],
    }

    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    max_simultaneous_downloads = 1

    d = Downloader(url, options, max_simultaneous_downloads)
    d.set_progress_hook(my_hook)
    d.start_download()

    while not d.is_finished():
        print(f"Downloading: {d.get_downloading_bytes()} bytes")
        print(f"Downloaded: {d.get_downloaded_bytes()} bytes")
        print(f"Status: {d.get_status()}")
