import redis

if __name__ == '__main__':
    r = redis.Redis(db=0)
    for key in r.keys():
        if 'hat' in key.decode('utf8'):
            print(f'{key} : {r.hgetall(key)}')
