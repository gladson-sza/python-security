import os

if __name__ == '__main__':
    host = input('Host: ')
    os.system('ping -n 6 {}'.format(host))
