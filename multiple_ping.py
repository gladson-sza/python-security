import os
import time

if __name__ == '__main__':
    with open('hosts.txt') as file:
        dump = file.read()
        dump = dump.splitlines()

        for ip in dump:
            print('-' * 60)
            os.system('ping -n 2 {}'.format(ip))
            time.sleep(2)
