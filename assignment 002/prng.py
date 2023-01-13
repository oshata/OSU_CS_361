
import random
import time


def random_num():
    print('prng.py running...')
    while True:
        time.sleep(1)
        start = 1
        end = 5
        with open("prng-service.txt", "r+") as file:
            line = file.readline()
            if line.strip() == "run":
                rand_num = random.randint(start, end)
                file.seek(0)
                file.write(str(rand_num))
                file.truncate()


if __name__ == '__main__':
    random_num()

