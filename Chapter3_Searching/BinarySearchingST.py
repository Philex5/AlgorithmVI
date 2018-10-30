# 有序数组中的二分查找
class BinarySearchingST:
    def __init__(self, keys, vals):
        if len(keys) != len(vals):
            print('The length of keys and values is not equal !')
            raise ValueError
        self.keys = keys
        self.vals = vals
        self.N = len(self.keys)

    def size(self):
        return self.N

    def get(self, key):
        if self.isEmpty():
            return
        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            return self.vals[i]
        else:
            return

    # 二分查找,成功则key返回所在的位置,否则返回小于key的键中最大的键的位置
    def rank(self, key):
        low = 0
        high = self.N - 1
        while low <= high:
            mid = (low + high) // 2
            if key == self.keys[mid]:
                return mid
            elif key > self.keys[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def isEmpty(self):
        return self.N == 0

    # 查找键,找到则更新值,否则创造新节点
    def put(self, key, val):
        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            self.vals[i] = val
            return
        self.vals.append(self.vals[self.N-1])
        self.keys.append(self.keys[self.N-1])
        for j in range(self.N-1, i, -1):
            self.vals[j] = self.vals[j-1]
            self.keys[j] = self.keys[j-1]
        self.vals[i] = val
        self.keys[i] = key

    # 返回最大的键
    def max(self):
        return self.keys[self.N-1]

    # 返回最小的键
    def min(self):
        return self.keys[0]

    def ceiling(self, key):
        i = self.rank(key)
        return self.keys[i]

    def floor(self, key):
        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            return self.keys[i]
        return self.keys[i+1]

    def delete(self, key):
        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            for j in range(i, self.N):
                self.keys[i] = self.keys[i+1]
                self.vals[i] = self.vals[i+1]
            self.keys.pop()
            self.vals.pop()
        else:
            print('no such key')

    def select(self, k):
        return self.keys[k]

    def keys(self, key_low, key_high):
        i = self.rank(key_low)
        j = self.rank(key_high)
        return self.keys[i:j]

if __name__ == '__main__':
    keys = ['a', 'b', 'c', 'g', 'z']
    vals = [1, 2, 3, 4, 5]
    bst = BinarySearchingST(keys, vals)
    print(bst.get('a'))
    bst.put('l', 6)
    print(bst.keys)
    bst.delete('l')
    print(bst.keys)












