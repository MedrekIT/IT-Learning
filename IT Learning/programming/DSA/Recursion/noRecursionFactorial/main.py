if __name__ == '__main__':
    x = int(input('Enter a number you want to get factorial of: '))

    y=1
    for i in range(1, x+1):
        y*=i

    print(x, 'factorial is', y)