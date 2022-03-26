import time
from threading import Thread


def car(speed, name):
    road = 0

    while road < 100:
        print(f'Car {name}: {road}\n')
        road += speed
        time.sleep(0.5)


if __name__ == '__main__':
    t_car1 = Thread(target=car, args=[10, '1'])
    t_car2 = Thread(target=car, args=[20, '2'])

    t_car1.start()
    t_car2.start()
