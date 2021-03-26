from __future__ import unicode_literals
import youtube_dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger('downloader')

url = 'url init'


def my_hook(d):
    if d['status'] == 'finished':
        print(f'Url {url} started...')
        print('Done downloading, now converting ...')


ytdl_opts = {
    'format': 'bestvideo/best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',            # avi/flv/mkv/mp4/ogg/webm
    }],
    'outtmpl': '~/Downloads/%(title)s.%(ext)s',
    'logger': logger,
    'progress_hooks': [my_hook],
}


def downloader(ytdl_opts, url):
    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        ytdl.download([url])


# Test
if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=wZnVQT_iEYo'
    downloader(ytdl_opts, url)
