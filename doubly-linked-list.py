class Item:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, val):
        newItem = Item(val)
        if self.head != None:
            newItem.next = self.head
            self.head.prev = newItem
        self.head = newItem

    def insertAtMiddle(self, val, pos):
        size = 0
        n = self.head
        while n != None:
            n = n.next
            size += 1
        if size+1 < pos:
            print('Out of bounds')
        elif pos == 0:
            self.insertAtBegin(val)
        else:            
            newItem = Item(val)
            curr = self.head
            for i in range(1, pos):
                curr = curr.next
            if curr.next != None:
                curr.next.prev = newItem
            newItem.next = curr.next
            newItem.prev = curr
            curr.next = newItem

    def insertAtEnd(self, val):
        newItem = Item(val)
        if self.head == None:
            self.insertAtBegin(val)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newItem
            newItem.prev = curr

    def removeAtBegin(self):
        if self.head == None:
            print('List empty')
        elif self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def removeAtMiddle(self, pos):
        size = 0
        n = self.head
        while n != None:
            n = n.next
            size += 1
        if self.head == None:
            print('List empty')
        elif size < pos:
            print('Out of bounds')
        elif self.head.next == None:
            self.head = None
        elif pos == 0:
            self.removeAtBegin()
        else:
            curr = self.head
            for i in range(1, pos):
                curr = curr.next
            curr.next = curr.next.next
            if curr.next != None:
                curr.next.prev = curr

    def removeAtEnd(self):
        if self.head == None:
            print('List Empty')
        elif self.head.next == None:
            self.head = None
        else:
            curr = self.head
            while curr.next.next != None:
                curr = curr.next
            curr.next = None

    def search(self, val):
        curr = self.head
        i = 0
        f = True
        while curr != None:
            if curr.val == val:
                print('Found at ' + str(i))
                f = False
                break
            i += 1
            curr = curr.next
        if f:
            print('Not found')

    def reverse(self):
        if self.head == None:
            print('List empty')
        elif self.head.next != None:            
            curr = self.head.next
            self.head.next = None
            self.head.prev = curr
            while curr.next != None:
                temp = curr.next
                curr.next = curr.prev
                curr.prev = temp
                curr = curr.prev
            self.head = curr
            curr.next = curr.prev
            curr.prev = None

    def display(self):
        curr = self.head
        while curr != None:
            print(curr.val+"->", end = '')
            curr = curr.next
        print('None')

ll1  = LinkedList()
ch = 1
while ch != 0:
    ch = int(input('Enter choice - '))
    if ch == 1:
        ll1.insertAtBegin(input('Enter value = '))
    elif ch == 2:
        ll1.insertAtMiddle(input('Enter value = '), int(input('Enter position = ')))
    elif ch == 3:
        ll1.insertAtEnd(input('Enter value = '))
    elif ch == 4:
        ll1.removeAtBegin()
    elif ch == 5:
        ll1.removeAtMiddle(int(input('Enter position = ')))
    elif ch == 6:
        ll1.removeAtEnd()
    elif ch == 7:
        ll1.search(input('Enter value = '))
    elif ch == 8:
        ll1.reverse()
    ll1.display()
