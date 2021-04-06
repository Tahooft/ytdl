
class FutureList:
    '''
    queue
    '''
    def __init__(self, queue):
        self._items = queue

    def __len__(self):
        return len(self._items)

    def __setitem__(self, key, value):
        self._items[key] = value

    def __getitem__(self, key):
        if type(key) is not int:
            raise Exception('Index must be an integer')
        return self._items[key]

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        while self._items:
            yield self._items


# Test
if __name__ == "__main__":

    myqueue = [
        'https://www.youtube.com/watch?v=v2r2riGruPM',
        'https://www.youtube.com/watch?v=yvxMlQrGLkM',
        'https://www.youtube.com/watch?v=nTasT5h0LEg',
        'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
        'https://www.youtube.com/watch?v=84U5NlBOD64',
        'https://www.youtube.com/watch?v=q9MAIwJMc1U',
        'https://www.youtube.com/watch?v=ya6yw7RPjGg',
        'https://www.youtube.com/watch?v=ALZmCy2u0jQ',
        'https://www.youtube.com/watch?v=qVpWpfD27mM',
        'https://www.youtube.com/watch?v=d0FV3_i-6WU+',
        ]

    future_list = FutureList(myqueue)
    print('Items #: %d' % len(future_list))
    # print(future_list._items)
    # print(future_list[3])

    for item in future_list:
        print(item)

    # print('While loop')
    # i = 0
    # while i < len(future_list):
    #     print(future_list[i])
    #     i += 1
