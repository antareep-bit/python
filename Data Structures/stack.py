class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.i = 0

    def empty(self):
        if self.top is None:
            return True
        else:
            return False

    def size(self):
        print(self.i)

    def f_top(self):
        print(id(self.top))

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.i += 1

    def pop(self):
        if self.empty():
            print('Empty')
        else:
            self.top = self.top.next

    def display(self):
        curr = self.top
        while curr:
            print(str(curr.val), end=', ')
            curr = curr.next
        print('None')


stack = Stack()
ch = -1
while ch != 0:
    ch = int(input('Enter choice - '))
    if ch == 1:
        if stack.empty():
            print('Empty')
        else:
            print('Not empty')
    elif ch == 2:
        stack.size()
    elif ch == 3:
        stack.f_top()
    elif ch == 4:
        stack.push(int(input('Enter value - ')))
    elif ch == 5:
        stack.pop()
    stack.display()
