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
        self.head = newItem

    def insertAtMiddle(self, val, pos):
        size = 0
        n = self.head
        while n != None:
            n = n.next
            size += 1
        newItem = Item(val)
        if size+1 <= pos:
                print('Out of bounds')
        elif pos == 0:
            newItem.next = self.head
            self.head = newItem
        else:
            curr = self.head
            for i in range(1, pos):
                curr = curr.next
            newItem.next = curr.next
            curr.next = newItem
    
    def insertAtEnd(self, val):
        newItem = Item(val)
        if self.head == None:
            self.head = newItem
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = newItem

    def removeAtBegin(self):
        if self.head != None:
            self.head = self.head.next
        else:
            print('List empty')

    def removeAtMiddle(self, pos):
        size = 0
        n = self.head
        while n != None:
            n = n.next
            size += 1
        if self.head == None:
            print('List empty')
        elif size-1 < pos:
            print('Out of bounds')
        elif pos == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for i in range(1, pos):
                curr = curr.next
            curr.next = curr.next.next
    
    def removeAtEnd(self):
        if self.head == None:
            print('List empty')
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
            prev = self.head
            curr = prev.next
            nxt = curr.next
            prev.next = None
            while nxt != None:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = curr.next
            self.head = curr
            curr.next = prev

    def display(self):
        curr = self.head
        while curr != None:
            print(curr.val+"->",end = '')
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
