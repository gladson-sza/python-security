import hashlib

if __name__ == '__main__':
    file1 = 'file1.txt'
    file2 = 'file2.txt'

    hash1 = hashlib.new('ripemd160')
    hash1.update(open(file1, 'rb').read())

    hash2 = hashlib.new('ripemd160')
    hash2.update(open(file2, 'rb').read())

    if hash1.digest() != hash2.digest():
        print(f'File {file1} is not equals to File {file2}')
        print(f'File 1 hash {hash1.hexdigest()}')
        print(f'File 2 hash {hash2.hexdigest()}')
    else:
        print(f'File {file1} is equals to File {file2}')
        print(f'File hash {hash1.hexdigest()}')
