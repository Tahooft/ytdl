import download1


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_download1():

url = 'https://www.youtube.com/watch?v=d0FV3_i-6WU+'

result = download1(ydl_opts, url)
