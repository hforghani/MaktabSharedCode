import time

from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')


@app.task
def add(x, y):
    return x + y


@app.task
def consume_some_time():
    t = time.time()
    for _ in range(10 ** 9):
        x = 9999 + 9999  # However it is a useless code!!!
    print(f'took {time.time() - t} s')
    return x
