import random
import string

if __name__ == '__main__':
    size = 16

    chars = string.ascii_letters + string.digits + '!@#$%&*()_-=+{}[]'

    rnd = random.SystemRandom()

    print(''.join(rnd.choice(chars) for i in range(size)))

