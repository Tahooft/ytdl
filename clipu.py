import time
import pyperclip as clipboard
from regulars import isValidURL
import youtu


def deloop():
    latest = ''
    clipped = 'go'

    while clipped != 'Stop':

        clipped = clipboard.paste()

        if clipped != latest:
            latest = clipped
            print('Changed!')

            if isValidURL(clipped):
                print('Valid url')
                youtu.download(youtu.ytdl_opts, clipped)

        print('\nclipped:', clipped, '\n')

        time.sleep(5)


# Test
if __name__ == "__main__":
    deloop()

# # copying text to clipboard
# clipboard.copy(text1)
# # pasting the text from clipboard
# text2 = clipboard.paste()
