import ipaddress


if __name__ == '__main__':
    ip = '192.168.0.1'
    address = ipaddress.ip_address(ip)
    print(address + 256)

    ip = '192.168.0.0/24'
    network = ipaddress.ip_network(ip, strict=False)
    print(network)

    for ip in network:
        print(ip)