class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def searchU(self, val):
        node = self.search(val, self.root)
        if node:
            print(node.data, 'found at ', node)
        else:
            print('Not found')

    def search(self, val, curr):
        if curr:
            if curr.data == val:
                return curr
            elif curr.data > val:
                return self.search(val, curr.left)
            else:
                return self.search(val, curr.right)
        else:
            return None

    def insertU(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert(val, self.root)

    def insert(self, val, curr):
        if curr.data < val:
            if curr.right is None:
                curr.right = Node(val)
                curr.right.parent = curr
            else:
                self.insert(val, curr.right)
        elif curr.data > val:
            if curr.left is None:
                curr.left = Node(val)
                curr.left.parent = curr
            else:
                self.insert(val, curr.left)

    def removeU(self, val):
        node = self.search(val, self.root)
        if node is None:
            print('Not found')
        else:
            self.remove(node)

    def remove(self, node):
        if node.left is None and node.right is None:
            self.rip(node, None)
        elif node.left is None or node.right is None:
            if node.left is None:
                self.rip(node, node.right)
            else:
                self.rip(node, node.left)
        else:
            succ = self.min(node.right)
            node.data = succ.data
            self.remove(succ)

    def rip(self, node1, node2):
        if node1 is self.root:
            self.root = node2
        else:
            if node1.parent.left is node1:
                node1.parent.left = node2
            else:
                node1.parent.right = node2
            if node2:
                node2.parent = node1.parent

    def min(self, curr):
        if curr.left:
            return self.min(curr.left)
        else:
            return curr

    def display(self, curr):
        if curr:
            self.display(curr.left)
            print(curr.data, end=', ')
            self.display(curr.right)


tree = BST()
ch = -1
while ch != 0:
    ch = int(input('Enter choice - '))
    if ch == 1:
        tree.searchU(int(input('Enter value - ')))
    elif ch == 2:
        tree.insertU(int(input('Enter value - ')))
    elif ch == 3:
        tree.removeU(int(input('Enter value - ')))
    tree.display(tree.root)