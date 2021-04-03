from __future__ import unicode_literals
import youtube_dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

url = 'url init'


def my_hook(d):
    if d['status'] == 'error':
        f = d['filename']
        logger.error('Error while downloading %s' % f)
        raise youtube_dl.utils.DownloadError('\nDownload error raised\n')
    elif d['status'] == 'downloading':
        logger.debug('%s downloading' % url)
        p = d['_percent_str']
        logger.debug('Downloaded so far: %s' % p)
        f = d['filename']
        logger.debug('Filename: %s' % f)
        e = d['_eta_str']
        logger.debug('Estimated time left: %s' % e)
        pass
    elif d['status'] == 'finished':
        f = d['filename']
        logger.info('\n<my_hook> Status finished: %s\n' % f)
        print('\n<my_hook> download of %s finished\n' % f)


ydl_opts = {
    'simulate': False,
    'quiet': False,
    'verbose': False,
    'no_warnings': False,
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '~/Downloads/%(title)s.%(ext)s',
    'logger': logger,
    'progress_hooks': [my_hook],
}


def download1(ydl_opts, url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except youtube_dl.utils.DownloadError as e:
            logger.error('\nYoutube_dl DownloadError at: %s' % url)
            logger.error(e)
        except Exception as e:
            logger.error('\nOther error at: %s' % e)
        else:
            logger.info('started downloading : %s' % url)
            result = 'started downloading %s' % url
            return result
        finally:
            logger.info('Downloader busy: %s' % url)
            result = 'Download busy: %s' % url
            return result

    return result


# Test
if __name__ == "__main__":
    # url = 'https://www.youtube.com/watch?v=qVpWpfD27mM'
    # url = 'https://www.youtube.com/watch?v=nTasT5h0LEg'   # Error test
    url = 'https://www.youtube.com/watch?v=d0FV3_i-6WU+'

    download1(ydl_opts, url)

    print("Ended and all that")
    logger.info('End of test')
