from __future__ import unicode_literals
import youtube_dl


url = 'https://www.youtube.com/watch?v=wZnVQT_iEYo'
url = ''

class MyLogger(object):

    def debug(self, msg):
        pass

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ytdl_opts = {
    'format': 'bestvideo/best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',            # avi/flv/mkv/mp4/ogg/webm
    }],
    'outtmpl': '~/Downloads/%(title)s.%(ext)s',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


def download(ytdl_opts, url):
    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        ytdl.download([url])


# Test
if __name__ == "__main__":
    download(ytdl_opts, url)
