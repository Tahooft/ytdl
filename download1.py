from __future__ import unicode_literals
import youtube_dl
import logging.config
import yaml

with open('./log.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

url = 'url init'
feedback = {'url': url}


def my_hook(d):
    """ Returns progress of youtube_dl(url)
        status
            If status is one of "downloading", or "finished",
            the following properties may also be present:
            * filename: The final filename (always present)
            * tmpfilename: The filename we're currently writing to
            * downloaded_bytes: Bytes on disk
            * total_bytes: Size of the whole file, None if unknown
            * total_bytes_estimate: Guess of the eventual file size,
                                    None if unavailable.
            * elapsed: The number of seconds since download started.
            * eta: The estimated time in seconds, None if unknown
            * speed: The download speed in bytes/second, None if
                    unknown
            * fragment_index: The counter of the currently
                                downloaded video fragment.
            * fragment_count: The number of fragments (= individual
                            files that will be merged)
    """

    if d['status'] == 'error':
        feedback['status'] = 'error'
        f = d['filename']
        feedback['filename'] = f
        logger.error('[mh] %s' % feedback)
        raise youtube_dl.utils.DownloadError('\n[mh] Download error raised\n')
    elif d['status'] == 'downloading':
        feedback['status'] = 'downloading'
        f = d['filename']
        feedback['filename'] = f
        # logger.debug('[mh] %s' % feedback)
    elif d['status'] == 'finished':
        feedback['status'] = 'finished'
        f = d['filename']
        feedback['filename'] = f
        # logger.debug('[mh] %s' % feedback)

    return feedback


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
    """
    Downloads url
        if download succeeded returns same url
        else returns False
    """
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except youtube_dl.utils.DownloadError as e:
            result = False
            logger.error('[d1]Youtube_dl DownloadError at: %s' % url)
            logger.error(e)
        except Exception as e:
            result = False
            logger.error('[d1]Other error at: %s' % e)
        else:
            result = url
            logger.info('[d1] Ended1: %s' % url)
        finally:
            return result


# Test
if __name__ == "__main__":

    # url = 'https://www.youtube.com/watch?v=xwGJYIWhZDM'   # Large file
    # url = 'https://www.youtube.com/watch?v=qVpWpfD27mM'
    # url = 'https://www.youtube.com/watch?v=nTasT5h0LEg'   # Error test
    url = 'https://www.youtube.com/watch?v=d0FV3_i-6WU+'

    result = download1(ydl_opts, url)

    logger.info('[d1 test] End of test')
    print('Done: %s\n' % result)

# Notes
# except youtube_dl.utils.DownloadError:
#                     pass
