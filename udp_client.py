import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = 'localhost'
    port = 5432

    message = 'Message to the server'

    try:
        print('Client message: ' + message)
        s.sendto(message.encode(), (host, port))

        data, server = s.recvfrom(4096)
        data = data.decode()

        print('Server message: ' + data)
    finally:
        print('Connection ended')
        s.close()


if __name__ == '__main__':
    main()
