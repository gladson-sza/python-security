import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    except socket.error as e:
        print('Connection fail: {}'.format(e))
        sys.exit()

    host = input('Host: ')
    port = int(input('Port: '))

    try:
        s.connect((host, port))
        print('Success connect to host {} at port {}'.format(host, port))
        s.shutdown(2)
    except socket.error as e:
        print('Connection fail: {}'.format(e))
        sys.exit()


if __name__ == '__main__':
    main()
