import itertools


if __name__ == '__main__':
    string = 'Password'
    result = itertools.permutations(string, len(string))

    for i in result:
        print(''.join(i))

