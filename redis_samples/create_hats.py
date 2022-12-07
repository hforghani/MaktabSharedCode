import random
import redis

if __name__ == '__main__':
    random.seed(444)
    hats = {f"hat:{random.getrandbits(32)}": i for i in (
        {
            "color": "black",
            "price": 49.99,
            "style": "fitted",
            "quantity": 1000,
            "npurchased": 0,
        },
        {
            "color": "maroon",
            "price": 59.99,
            "style": "hipster",
            "quantity": 500,
            "npurchased": 0,
        },
        {
            "color": "green",
            "price": 99.99,
            "style": "baseball",
            "quantity": 200,
            "npurchased": 0,
        })
            }

    r = redis.Redis(db=0)

    with r.pipeline() as pipe:
        for h_id, hat in hats.items():
            pipe.hset(h_id, mapping=hat)
        pipe.execute()

    print('hats saved successfully')
    r.bgsave()  # to persist in the db
