# i want a python class that takes an url as parameter and then start an instance of yt-dlp to download the file stated in that url.
# i want to be able to set all the options for yt-dlp.
# i want to keep track of the progress of the download
# if the download has succeeded it returns the url otherwise the boolean FALSE
# I want to limit the maximimum of simultanious downloading yt-dlp instances to be 5


import yt_dlp


class Downloader:
    def __init__(self, url, options):
        self.url = url
        self.options = options
        self.progress = 0

    def download(self):
        with yt_dlp.YoutubeDL(self.options) as ydl:
            ydl.add_progress_hook(self.progress_hook)
            try:
                ydl.download([self.url])
                return self.url
            except:
                return False

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            self.progress = d['_percent_str']


# You can set all the options for yt_dlp in the options dictionary.
# For example, if you want to download the best quality video and audio, you can set the format option to 'bestvideo+bestaudio'.
# You can find more information about the available options in the official documentation.
# The download method returns the URL if the download has succeeded, otherwise it returns False.
# The progress of the download is stored in the progress attribute of the Downloader instance.
# You can access it at any time to keep track of the progress of the download.
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
options = {
    # set all the options here
    'format': 'bestvideo[height<=2720]+bestaudio/best[height<=2720]',
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4'
    }]

}
downloader = Downloader(url, options)
url_or_false = downloader.download()

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
