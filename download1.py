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
        logger.error('[mh] Error while downloading %s' % f)
        raise youtube_dl.utils.DownloadError('\n[mh] Download error raised\n')
    elif d['status'] == 'Downloading':
        logger.debug('[mh] Downloading: %s' % url)
        p = d['_percent_str']
        logger.debug('[mh] Downloaded so far: %s' % p)
        f = d['filename']
        logger.debug('[mh] Filename: %s' % f)
        e = d['_eta_str']
        logger.debug('[mh] Estimated time left: %s' % e)
    elif d['status'] == 'finished':
        f = d['filename']
        logger.info('[mh] Status finished: %s' % f)
        print('[mh] Download of %s finished' % f)


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
            result = '[d1]Youtube_dl DownloadError at: %s' % url
            logger.error('[d1]Youtube_dl DownloadError at: %s' % url)
            logger.error(e)
        except Exception as e:
            result = '[d1]Other error at: %s' % e
            logger.error('[d1]Other error at: %s' % e)
        else:
            result = '[d1] Started:  %s' % url
            logger.debug('[d1]Started: %s' % url)
        finally:
            return result


# Test
if __name__ == "__main__":

    from time import sleep
    # url = 'https://www.youtube.com/watch?v=xwGJYIWhZDM'   # Large file
    # url = 'https://www.youtube.com/watch?v=qVpWpfD27mM'
    # url = 'https://www.youtube.com/watch?v=nTasT5h0LEg'   # Error test
    url = 'https://www.youtube.com/watch?v=d0FV3_i-6WU+'

    download1(ydl_opts, url)

    print("Ended and all that now waiting 10 secs")
    logger.debug('[d1 test] End of test')
    sleep(10)
    print('Done')
