
class Record:
    '''
    Record class

    Recordveld id's in constants voor gemak
        future          None
        url             'url'
        filename        ''
        percent_done    n%
        est_time_left   False
        error           False
        status          unknown/started/downloading/done
    '''

    def __init__(self, record):
        self._index = -1
        self._record = record

    def __len__(self):
        return len(self._record)

    def __setitem__(self, key, value):
        self._record[key] = value

    def __getitem__(self, key):
        if type(key) is not int:
            raise Exception('Index must be an integer')
        return self._record[key]

    def __contains__(self, item):
        return item in self._record

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index >= len(self._record):
            self.index = -1
            raise StopIteration
        else:
            return self._record[self._index]


# Test
if __name__ == "__main__":

    fields = [
            'future',
            'status',
            'url',
            'filename',
            'percent_done',
            'est_time_left',
            'error',
    ]

    newrecord = Record(fields)

    print('\nTest __getitem__')
    print(newrecord[2])

    print('\nTest __next__')
    for field in newrecord:
        print(field)

    print('\nTest __next__')
    i = 0
    while i < len(newrecord):
        print(newrecord[i])
        i += 1
