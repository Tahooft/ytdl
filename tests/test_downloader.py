import pytest
from downloader import Downloader


@pytest.fixture
def downloader():
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'progress_hooks': [lambda status: None],
    }
    max_simultaneous_downloads = 1
    return Downloader(url, options, max_simultaneous_downloads)


def test_get_url(downloader):
    assert downloader.get_url() == 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'


def test_set_progress_hook(downloader):
    def my_hook(status):
        pass
    downloader.set_progress_hook(my_hook)
    assert downloader.get_progress_hook() == my_hook


def test_get_status(downloader):
    assert downloader.get_status() == 'not started'


def test_get_downloading_bytes(downloader):
    assert downloader.get_downloading_bytes() == 0


def test_get_downloaded_bytes(downloader):
    assert downloader.get_downloaded_bytes() == 0


def test_is_finished(downloader):
    assert not downloader.is_finished()
