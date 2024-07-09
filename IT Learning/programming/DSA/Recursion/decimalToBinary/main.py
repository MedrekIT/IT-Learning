def decimaltobinary(x):
    if x > 0:
        decimaltobinary(x // 2)
        print(x % 2, end='')


if __name__ == '__main__':
    x = int(input('Enter a decimal number: '))

    print('Number', x, 'is', end=' ')
    decimaltobinary(x)
    print(' in binary code')