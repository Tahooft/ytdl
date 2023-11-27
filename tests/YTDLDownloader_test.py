import pytest
from unittest.mock import patch
from ytdl_downloader import YTDLDownloader


@pytest.fixture
def downloader():
    return YTDLDownloader()


def test_download_success(downloader):
    url = 'https://www.youtube.com/watch?v=ZjjbajOR-H4'
    options = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'nooverwrites': True,
        'continuedl': True,
        'quiet': True,
        'no_warnings': True,
        'restrictfilenames': True,
        'ignoreerrors': True,
        'socket_timeout': 5,
        'retries': 3,
        'fragment_retries': 3,
        'skip_unavailable_fragments': True,
        'external_downloader': 'aria2c',
        'external_downloader_args': ['-x', '16', '-s', '16', '-k', '1M'],
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }]
    }
    with patch('ytdl_downloader.YoutubeDL') as mock_ydl:
        mock_ydl.return_value.download.return_value = None
        filename = downloader.download(url, options)
        assert filename == 'index.html.mp4'


def test_download_failure(downloader):
    url = 'https://www.example.com/invalid.html'
    options = {}
    with patch('ytdl_downloader.YoutubeDL') as mock_ydl:
        mock_ydl.return_value.download.return_value = None
        filename = downloader.download(url, options)
        assert filename is False
