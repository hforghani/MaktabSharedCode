import time


def add(x, y):
    return x + y


if __name__ == '__main__':
    t = time.time()
    for i in range(10 ** 8):
        add(9999, 9999)
        if i % 10 ** 7 == 0:
            print(i)
    print(f'took {time.time() - t} s')
