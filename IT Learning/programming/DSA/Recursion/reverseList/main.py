def revlistrec(t, n):
    if n >= len(t) // 2:
        return
    temp = t[n]
    t[n] = t[len(t) - n - 1]
    t[len(t) - n - 1] = temp
    return revlistrec(t, n + 1)


if __name__ == '__main__':
    s = int(input('Enter list size: '))
    t = [0] * s

    for i in range(s):
        t[i] = int(input('Enter ' + str(i + 1) + ' list element: '))

    revlistrec(t, 0)

    print(t)
