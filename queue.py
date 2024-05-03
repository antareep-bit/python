class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.end = None

    def enqueue(self, val):
        if self.end is None:
            self.end = Node(val)
            self.front = self.end
        else:
            self.end.next = Node(val)
            self.end = self.end.next

    def dequeue(self):
        if self.front is None:
            print('Underflow')
        else:
            print('Popped element - ' + str(self.front.val))
            self.front.next = self.front

    def f_front(self):
        print('Front = ' + str(self.front))

    def rear(self):
        print('Rear = ' + self.rear())


queue = Queue()
ch = -1
while ch != 0:
    ch = int(input('Enter choice - '))
    if ch == 1:
        queue.enqueue(int(input('Enter value - ')))
    elif ch == 2:
        queue.dequeue()
    elif ch == 3:
        queue.f_front()
    elif ch == 4:
        queue.rear()