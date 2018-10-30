import numpy as np
class MaxHeap:
    def __init__(self, origin_arr):
        self.len = len(origin_arr)
        self.arr = []
        self.arr.append(0)
        for i in range(self.len):
            self.arr.append(origin_arr[i])

    def less(self, a, b):
        return a < b

    def delMax(self):
        self.arr[1] = self.arr[self.len]
        self.arr.pop()
        self.len -= 1
        self.sink(1)
    # 上浮
    def swim(self, p):
        while self.arr[p] > self.arr[p//2]:
            self.arr[p], self.arr[p//2] = self.arr[p//2], self.arr[p]
            p = p // 2
    # 下沉
    def sink(self, p):
        while 2 * p <= self.len:
            k = 2 * p
            if k < self.len and self.less(self.arr[k], self.arr[k+1]):
                k += 1
            if not self.less(self.arr[p], self.arr[k]):
                break
            self.arr[p], self.arr[k] = self.arr[k], self.arr[p]
            p = k

    def insert(self, a):
        self.arr.append(a)
        self.len += 1
        self.swim(self.len)


key = ['T', 'P', 'R', 'N', 'H', 'O', 'A', 'E', 'I',  'G']
hp = MaxHeap(key)
print('origin_arr')
print(hp.arr)
print('Insert S:')
hp.insert('S')
print(hp.arr)
print('Delete T:')
hp.delMax()
print(hp.arr)






