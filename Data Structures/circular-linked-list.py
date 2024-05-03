class Item:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, val):
        newItem = Item(val)
        newItem.next = self.head
        if self.head == None:
            newItem.next = newItem
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = newItem
        self.head = newItem

    def insertAtMiddle(self, val, pos):
        size = 0
        curr = self.head
        if self.head != None:
            while curr.next != self.head:
                curr = curr.next
                size += 1
        if pos == 0:
            self.insertAtBegin(val)
        elif size+1 < pos:
            print('Out of bounds')
        else:
            newItem = Item(val)
            curr = self.head
            for i in range(1, pos):
                curr = curr.next
            newItem.next = curr.next
            curr.next = newItem

    def insertAtEnd(self, val):
        if self.head == None:
            self.insertAtBegin(val)
        else:
            newItem = Item(val)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = newItem
            newItem.next = self.head

    def removeAtBegin(self):
        if self.head == None:
            print('List empty')
        elif self.head.next == self.head:
            self.head = None
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next

    def removeAtMiddle(self, pos):
        size = 0
        curr = self.head
        if self.head != None:
            while curr.next != self.head:
                curr = curr.next
                size += 1
        if size < pos:
            print('Out of bounds')
        elif self.head == None:
            print('List empty')
        elif self.head.next == self.head:
            self.head = None
        elif pos == 0:
            self.removeAtBegin()
        else:
            curr = self.head
            for i in range(1, pos):
                curr = curr.next
            curr.next = curr.next.next
            if pos == 0:
                self.head = self.head.next

    def removeAtEnd(self):
        if self.head == None:
            print('List empty')
        elif self.head.next == self.head:
            self.head = None
        else:
            curr = self.head
            while curr.next.next != self.head:
                curr = curr.next
            curr.next = self.head

    def search(self, val):
        f = True
        i = 0
        curr = self.head
        if curr != None:
            while curr.next != self.head:
                if curr.val == val:
                    print('Found at ' + str(i))
                    f = False
                    break
                i += 1
                curr = curr.next
            if curr.val == val and f:
                print('Found at ' + str(i))
                f = False
        if f:
            print('Not found')

    def reverse(self):
        if self.head == None:
            print('List empty')
        else:
            prev = self.head
            curr = self.head.next
            nxt = curr.next
            while curr != self.head:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = curr.next
            self.head.next = prev
            self.head = prev

    def display(self):
        curr = self.head
        if curr != None:
            while curr.next != self.head:
                print(curr.val+"->", end = '')
                curr = curr.next
            print(curr.val+"->", end = '')
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
