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
        f = d['filename']
        logger.error(f'Error while downloading {f}')
        raise youtube_dl.utils.DownloadError('\nDownload error raised\n')
    elif d['status'] == 'downloading':
        logger.debug(f'Url {url} downloading')
        p = d['_percent_str']
        logger.debug(f'Downloaded so far: {p}')
        f = d['filename']
        logger.debug(f'Filename: {f}')
        e = d['_eta_str']
        logger.debug(f'Estimated time left: {e}')
        pass
    elif d['status'] == 'finished':
        f = d['filename']
        logger.info(f'\n<my_hook> Status finished: {url} {f}\n')
        print(f'\n<my_hook> download of {url} {f} finished\n')


ytdl_opts = {
    'simulate': False,
    'quiet': False,
    'verbose': False,
    'no_warnings': False,
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '~/Downloads/%(title)s.%(ext)s',
    'logger': logger,
    'progress_hooks': [my_hook],
}


def downloader(ytdl_opts, url):
    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        try:
            ytdl.download([url])
        except youtube_dl.utils.DownloadError as e:
            logger.error(f'\nYoutube_dl DownloadError at: {url}')
            logger.error(e)
        except Exception as e:
            logger.error(f'\nOther error at: {url}')
            logger.debug(f'Youtube_dl error:\n {e}')
        else:
            logger.info(f'started downloading : {url}')
            result = f'started downloading {url}'
            return result
        finally:
            logger.info(f'Downloader busy: {url}')
            result = f'Download busy: {url}'
            return result

    return result


# Test
if __name__ == "__main__":
    # url = 'https://www.youtube.com/watch?v=qVpWpfD27mM'
    # url = 'https://www.youtube.com/watch?v=nTasT5h0LEg'   # Error test
    url = 'https://www.youtube.com/watch?v=d0FV3_i-6WU+'

    downloader(ytdl_opts, url)

    print("Ended and all that")
    logger.info('End of test')
