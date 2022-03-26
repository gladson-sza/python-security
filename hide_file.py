import ctypes

if __name__ == '__main__':
    hidden_attr = 0x02
    result = ctypes.windll.kernel32.SetFileAttributesW('file1.txt', hidden_attr)

    if result:
        print('File hidden')
    else:
        print('File not hidden')