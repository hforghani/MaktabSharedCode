import time
from celery import Celery

app = Celery('myadd', backend='redis://localhost', broker='redis://localhost')


@app.task
def add():
    t = time.time()
    for _ in range(10 ** 9):
        x = 9999 + 9999  # However it is a useless code!!!
    print(f'took {time.time() - t} s')
    return x


results = []
count = 10
for _ in range(count):
    res = add.delay()
    results.append(res)

ready = set()
while len(ready) < count:
    time.sleep(3)
    for res in results:
        if res not in ready and res.ready():
            print(res.get())
            ready.add(res)
