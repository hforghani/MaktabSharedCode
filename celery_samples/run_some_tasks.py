import time
from tasks import consume_some_time

results = []
count = 5
for _ in range(count):
    res = consume_some_time.delay()
    results.append(res)

ready = set()
while len(ready) < count:
    time.sleep(3)
    for res in results:
        if res not in ready and res.ready():
            print(res.get())
            ready.add(res)
