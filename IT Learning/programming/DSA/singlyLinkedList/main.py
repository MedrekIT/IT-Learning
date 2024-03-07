class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertHead(self, val):
        newN = Node(val)
        if self.size == 0:
            self.head = newN
        else:
            newN.next = self.head
            self.head = newN
        self.size += 1

    def insertIndex(self, val, ind):
        if ind < 0 or ind > self.size:
            print("invalid index, that is not in range of a list!")
        elif ind == 0:
            self.insertHead(val)
        elif ind == self.size + 1:
            self.insertTail(val)
        else:
            newN = Node(val)
            curr = self.head
            for i in range(ind - 2):
                curr = curr.next
            newN.next = curr.next
            curr.next = newN
            self.size += 1

    def insertTail(self, val):
        newN = Node(val)
        if self.size == 0:
            self.head = newN
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newN
        self.size += 1

    def deleteHead(self):
        if self.size == 0:
            print('There are no elements in a list!')
        elif self.size > 1:
            self.head = self.head.next
            self.size -= 1
        else:
            self.head = None
            self.size = 0

    def deleteTail(self):
        if self.size == 0:
            print('There are no elements in a list!')
        elif self.size == 1:
            self.head = None
            self.size = 0
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            self.size -= 1

    def deleteIndex(self, ind):
        if self.size == 0:
            print('There are no elements in a list!')
        elif ind < 0 or ind > self.size:
            print("invalid index, that is not in range of a list!")
        elif ind == 0:
            self.deleteHead()
        elif ind == self.size:
            self.deleteTail()
        else:
            curr = self.head
            for i in range(ind - 2):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1

    def showEl(self):
        curr = self.head
        for i in range(self.size):
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def showLen(self):
        print('List is ' + str(self.size) + ' elements long')


if __name__ == '__main__':
    myLL = linkedList()
    print('Welcome to LInked List in Python programming language!')
    print('Menu:')
    print('1. Add element at head of a list')
    print('2. Add element at tail of a list')
    print('3. Add element at index of a list (iterrating from 1)')
    print('4. Delete element at head of a list')
    print('5. Delete element at tail of a list')
    print('6. Delete element at index of a list (iterrating from 1)')
    print('7. Show all elements')
    print('8. Show length of a list')
    print('9. Exit')
    while True:
        x = int(input('Choose from menu: '))
        if x == 1:
            val = int(input('Enter a value: '))
            myLL.insertHead(val)
        elif x == 2:
            val = int(input('Enter a value: '))
            myLL.insertTail(val)
        elif x == 3:
            val = int(input('Enter a value: '))
            ind = int(input('Enter an index: '))
            myLL.insertIndex(val, ind)
        elif x == 4:
            myLL.deleteHead()
        elif x == 5:
            myLL.deleteTail()
        elif x == 6:
            ind = int(input('Enter an index: '))
            myLL.deleteIndex(ind)
        elif x == 7:
            myLL.showEl()
        elif x == 8:
            myLL.showLen()
        elif x == 9:
            exit()
        else:
            print('Invalid choice, there is no such position in the menu!')
