
class Queue:
    '''
    Queue class

    [d1]: download1 hook generated feedback
    [x]:  downloadx feedback
    [f]:  running future feedback

        recordveld id's in constants voor gemak
        maxrunners = n
        running - started/downloading runners
        init
            queue begint met 1 url
            extend met rest van record velden
                url = 'url'
                status = unknown/started/downloading/ done/finished(?)
                % done - 0
                est time left - False
                future - None
                error - False
    '''

    # list of records

    def __init__(self):
        self.queue = ['init', 'url']
        self._index = -1

    def __len__(self):
        return len(self)

    def __setitem__(self, key, value):
        self[key] = value

    def __getitem__(self, key):
        if type(key) is not int:
            raise Exception('Index must be an integer')
        return self[key]

    def __contains__(self, item):
        return item in self

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self):
            self.index = -1
            raise StopIteration
        else:
            return self[self._index]


q = Queue()


# Test
if __name__ == "__main__":

    print('\nTest __getitem__')
    print(q.queue[1])

    print('\nTest __next__')
    for field in q.queue:
        print(field)

    print('\nTest __next__')
    i = 0
    while i < len(q.queue):
        print(q.queue[i])
        i += 1
