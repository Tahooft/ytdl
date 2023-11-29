# i want a class that will start and run a given number (parameter) of instances of Downloader simultaneously and print the finished url's


from concurrent.futures import ThreadPoolExecutor
from downloader import Downloader


class DownloaderManager:
    def __init__(self, urls, options, max_simultaneous_downloads):
        self.urls = urls
        self.options = options
        self.max_simultaneous_downloads = max_simultaneous_downloads
        self.downloaders = []
        self.finished_urls = []

    def start_downloads(self):
        with ThreadPoolExecutor(max_workers=self.max_simultaneous_downloads) as executor:
            for url in self.urls:
                downloader = Downloader(
                    url, self.options, self.max_simultaneous_downloads)
                self.downloaders.append(downloader)
                executor.submit(downloader.start_download)

    def print_finished_urls(self):
        for downloader in self.downloaders:
            if downloader.is_finished() and downloader.get_status() == 'finished':
                self.finished_urls.append(downloader.get_url())
        print(self.finished_urls)


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

    urls = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'https://www.youtube.com/watch?v=2ZIpFytCSVc']
    max_simultaneous_downloads = 2

    dm = DownloaderManager(urls, options, max_simultaneous_downloads)
    dm.start_downloads()
    dm.print_finished_urls()
