import pytest
from downloader import Downloader

@pytest.fixture
def downloader():
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    options = {
        # set all the options here
    }
    return Downloader(url, options)

def test_download(downloader):
    url_or_false = downloader.download()
    assert url_or_false == 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' or url_or_false == False
