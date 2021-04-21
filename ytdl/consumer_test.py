from consumer import ConsumerThread, queue, SENTINEL


# long_list = [
#     'https://www.youtube.com/watch?v=qE8PG2mpo58',
#     'https://www.youtube.com/watch?v=v2r2riGruPM',
#     'https://www.youtube.com/watch?v=yvxMlQrGLkM',
#     'https://www.youtube.com/watch?v=gm3dSYAWiUk',
#     'https://www.youtube.com/watch?v=nTasT5h0LEg',
#     'https://www.youtube.com/watch?v=7Ht9jkWXqlU',
#     'https://www.youtube.com/watch?v=84U5NlBOD64',
#     'https://www.youtube.com/watch?v=q9MAIwJMc1U',
#     'https://www.youtube.com/watch?v=ya6yw7RPjGg',
#     'https://www.youtube.com/watch?v=ALZmCy2u0jQ',
#     'https://www.youtube.com/watch?v=qVpWpfD27mM',
#     'https://www.youtube.com/watch?v=d0FV3_i-6WU+',
#     'https://www.youtube.com/watch?v=2KxJ6eTY9bA',
#     SENTINEL
# ]

short_list = [
    SENTINEL
]


def test_consumer_success():
    for url in short_list:
        queue.put(url)
        result = ConsumerThread().start()
    assert result is None


# print(queue.qsize)
# print(SENTINEL)
# for url in short_list:
#     queue.put(url)

# print(queue.qsize())

# result = ConsumerThread().start()
# print(result)
