import random

def rand_emoji():
    s = b'\U0001F'
    for _ in range(3):
        s += hex(random.randint(0,15))[2]
    return s.encode()
