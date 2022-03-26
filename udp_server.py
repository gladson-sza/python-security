import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = 'localhost'
    port = 5432

    s.bind((host, port))
    message = 'Server, response to client'

    while True:
        data, end = s.recvfrom(4096)

        if data:
            print('Sending message...')
            s.sendto(data + message.encode(), end)


if __name__ == '__main__':
    main()
