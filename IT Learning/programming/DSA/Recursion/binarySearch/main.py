def binarysearch(x, t, mid, left, right):
    if t[mid] == x:
        return mid
    elif t[mid] > x:
        return binarysearch(x, t, (mid + left) // 2, left, mid)
    else:
        return binarysearch(x, t, (mid + right) // 2, mid, right)


if __name__ == '__main__':
    s = int(input('Enter list size: '))
    t = [0] * s

    for i in range(s):
        t[i] = int(input('Enter ' + str(i + 1) + ' list element: '))

    t.sort()

    print('Sorted list:', t)

    x = int(input('Enter the element you would like to find: '))

    print('This is number', binarysearch(x, t, s // 2, 0, s - 1) + 1, 'element of a list')
