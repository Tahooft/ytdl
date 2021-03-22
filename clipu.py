import time
import pyperclip as clipboard
from regulars import isValidURL


def deloop():
    latest = ''
    clipped = 'go'

    while clipped != 'Stop':

        clipped = clipboard.paste()

        if clipped != latest:
            latest = clipped
            print('Changed!')

            if isValidURL(clipped):
                print('Valid')

        print('\nclipped:', clipped, '\n')

        time.sleep(5)


deloop()

# # copying text to clipboard
# clipboard.copy(text1)

# # pasting the text from clipboard
# text2 = clipboard.paste()
