import time
import pyperclip as clipboard
from regulars import isValidURL
import downloader as dl


def looper():
    latest = ''
    clipboard.copy('go')

    while clipboard.paste() != 'Stop':

        if clipboard.paste() != latest:
            print('Changed!')
            latest = clipboard.paste()

            if isValidURL(latest):
                print('Valid url')
                dl.downloader(dl.ytdl_opts, latest)

        print('\nclipped:', latest, '\n')

        time.sleep(5)


# Test
if __name__ == "__main__":
    looper()
