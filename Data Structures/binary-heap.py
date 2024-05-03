class Heap:
    def __init__(self):
        self.ilist = []
        self.index = 0

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def insert(self, val):
        self.ilist.append(val)
        self.index += 1
        i = self.index-1
        while i != 0:
            if self.ilist[self.parent(i)] > self.ilist[i]:
                self.ilist[self.parent(i)], self.ilist[i] = self.ilist[i], self.ilist[self.parent(i)]
                i = self.parent(i)
            else:
                break

    def getMin(self):
        return self.ilist[0]

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        min = i
        if l < self.index:
            if self.ilist[l] < self.ilist[i]:
                min = l
        if r < self.index:
            if self.ilist[r] < self.ilist[min]:
                min = r
        if self.ilist[min] != self.ilist[i]:
            self.ilist[min], self.ilist[i] = self.ilist[i], self.ilist[min]
            self.heapify(min)

    def extractMin(self):
        self.ilist[0], self.ilist[self.index-1] = self.ilist[self.index-1], self.ilist[0]
        del self.ilist[self.index-1]
        self.index -= 1
        self.heapify(0)

    def decreaseKey(self, pos, new_value):
        self.ilist[pos] -= new_value
        self.heapify(pos)

    def remove(self, val):
        if val not in self.ilist:
            print('Not found')
        else:
            pos = self.ilist.index(val)
            self.ilist[pos], self.ilist[self.index-1] = self.ilist[self.index-1], self.ilist[pos]
            del self.ilist[self.index-1]
            self.index -= 1
            self.heapify(self.index-1)

    def display(self):
        print(self.ilist)


bheap = Heap()
ch = -1
while ch != 0:
    ch = int(input('Enter choice - '))
    if ch == 1:
        bheap.insert(int(input('Enter value - ')))
    elif ch == 2:
        bheap.remove(int(input('Enter value - ')))
    elif ch == 3:
        bheap.extractMin()
    bheap.display()