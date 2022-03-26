import hashlib

if __name__ == '__main__':
    hash_md5 = hashlib.md5(b'Python security')
    hash_sha1 = hashlib.sha1(b'Python security')
    hash_sha256 = hashlib.sha256(b'Python security')
    hash_sha512 = hashlib.sha512(b'Python security')

    print(f'Hash MD5: {hash_md5.hexdigest()}')
    print(f'Hash SHA1: {hash_sha1.hexdigest()}')
    print(f'Hash SHA256: {hash_sha256.hexdigest()}')
    print(f'Hash SHA512: {hash_sha512.hexdigest()}')