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
    if d['status'] == 'error':
        logger.error('Error while downloading')
    elif d['status'] == 'downloading':
        logger.debug(f'Url {url} downloading')
        # p = d['_percent_str']
        # logger.debug('Downloaded so far: {}'.format(p))
        f = d['filename']
        logger.debug(f'Filename: {f}')
        e = d['_eta_str']
        logger.debug(f'Estimated time left: {e}')
    elif d['status'] == 'finished':
        logger.debug('Done downloading')


ytdl_opts = {
    'format': 'bestvideo/bestaudio',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',            # avi/flv/mkv/mp4/ogg/webm
    }],
    'outtmpl': '~/Downloads/%(title)s.%(ext)s',
    'logger': logger,
    'quiet': True,
    'progress_hooks': [my_hook],
}


def downloader(ytdl_opts, url):
    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        ytdl.download([url])


# Test
if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=wZnVQT_iEYo'
    downloader(ytdl_opts, url)

# # more ydtl_opts
    # 'format': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
    # 'writethumbnail': True,
    # 'writesubtitles': True,
    # 'writeautomaticsub': True,
    # 'subtitleslangs': 'en',
