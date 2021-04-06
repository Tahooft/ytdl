
'''
Queue class
    recordveld id's in constants voor gemak
    running - #started
    init
        queue begint met 1 url
        extend met rest van record velden
            url = 'url'
            andere velden 0 of False ...

'''
# record = [
#          'url',
#          'filename',
#          'started',
#          'done',
#          'downloading',
#          'percent_done',
#          'est_time_left',
#          'finished',
#          'error',
#          'future',
#         ]

record = [
         'url',
         'name',
         's',
         'done',
         'dload',
         'pdone',
         'est',
         'fin',
         'err',
         'fut',
        ]

urls = [
    'v2r2riGruPM',
    'yvxMlQrGLkM',
    'nTasT5h0LEg',
    '7Ht9jkWXqlU',
    '84U5NlBOD64',
    'q9MAIwJMc1U',
    'ya6yw7RPjGg',
    'ALZmCy2u0jQ',
    'qVpWpfD27mM',
    'd0FV3_i-6WU+',
    ]

queue = []

i = 0
while i < len(urls):
    temp = []
    temp.append(urls[i])
    temp.extend(record)
    queue.append(temp)
    i += 1

queue[1][4] = 999
print(queue[3][4])

# Test

# if __name__ == "__main__":

#     i = 0
#     while i < len(queue):
#         print(queue[i])
#         i += 1

# print()
