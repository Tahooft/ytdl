import pytest
import download1 as dl


def test_download_success():
    url = 'https://www.youtube.com/watch?v=d0FV3_i-6WU+'
    result = dl.download1(url)
    assert result == {url: 'Downloaded'}


def test_download_error():
    novideo = 'https://www.youtube.com/watch?v=nTasT5h0LEg'
    result = dl.download1(novideo)
    assert result == {novideo: 'DownloadError'}


def test_download_junk():
    junk = 'junklink'
    result = dl.download1(junk)
    assert result == {junk: 'DownloadError'}


def test_download_typeerror():
    with pytest.raises(TypeError):
        result = dl.download1()
        assert result == 'Nothing to see here'


def test_download_empty():
    """ This one should give a result not the exception """
    result = dl.download1()
    assert result == 'error of zo'
