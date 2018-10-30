
# 利用链表实现先进后出的栈和先进先出的队列

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Linklist_Stack:
    def __init__(self, first):
        self.first = first
        self.N = 1

    def push(self, element):
        oldfirst = self.first
        first = Node(element, oldfirst)
        self.first = first
        self.N += 1

    def pop(self):
        if self.IsEmpty():
            print('Queue is Empty!')
            return
        node = self.first
        self.first = self.first.next
        self.N -= 1
        return node.item

    def IsEmpty(self):
        return self.N == 0

    def Size(self):
        return self.N


class Linklist_Queue:
    def __init__(self, first):
        self.first = first
        self.N = 1

    def push(self, element):
        oldfirst = self.first
        first = Node(element, oldfirst)
        self.first = first
        self.N += 1

    def pop(self):
        if self.IsEmpty():
            print('Queue is Empty!')
            return
        node = self.first
        nums = self.Size()
        while nums > 1 :
            node = node.next
            nums -= 1
        item = node.item
        self.N -= 1
        return item

    def IsEmpty(self):
        return self.N == 0

    def Size(self):
        return self.N


if __name__ == '__main__':
    first  = Node(1,None)
    ls = Linklist_Queue(first)
    for i in range(10):
        ls.push(i+2)
        print(ls.Size())

    for i in range(12):
        print(ls.pop())