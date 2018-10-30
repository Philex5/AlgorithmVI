# 顺序查找(基于无序链表)
class Node:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next


class SequentialSearchSt:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.first = nodes[0]

    # 查找给定的键,并返回相关联的值
    def get(self, key):
        pos = self.first
        while pos is not None:
            if pos.key == key:
                return pos.val
            pos = pos.next
        print('No Such Key!')
        return

    # 查找给定的键,找到则更新其值,否则在表中新建节点
    def put(self, key, val):
        pos = self.first
        while pos is not None:
            if pos.key == key:
                pos.val = val
                return
            pos = pos.next
        self.first = Node(key, val, self.first)
        return

    # 统计表中键值对的数量
    def size(self):
        pos = self.first
        count = 0
        while pos is not None:
            pos = pos.next
            count += 1
        return count

    # 表中数据按键排序
    def key(self):
        pos = self.first
        keys = []
        while pos is not None:
            keys.append(pos.key)
            pos = pos.next
        return sorted(keys)


    # 删除指定的键和它对应的值
    def delete(self, key):
        pos1 = self.first
        if pos1 is None:
            return
        if pos1.next is None:
            if pos1.key == key:
                self.first = None
            else:
                print('No such key')
            return
        pos2 = pos1.next
        if pos1.next == key:
            self.first = pos2
            return
        while pos2 is not None:
            if pos2.key == key:
                pos1.next = pos2.next
            pos1 = pos2
            pos2 = pos2.next
        print('No such key')


if __name__ == '__main__':
    keys = ['b', 'n', 'a', 'g', 'z']
    vals = [1, 2, 3, 4, 5]
    nodes = []
    for i in range(len(keys)):
        node = Node(keys[i], vals[i], None)
        nodes.append(node)
    for i in range(len(keys)-1):
        nodes[i].next = nodes[i+1]
    for i in range(len(keys)):
        print(nodes[i].next)

    sst = SequentialSearchSt(nodes)
    print('fisrt: ', sst.first.key)
    print(sst.get('a'))
    sst.put('z', 6)
    print(sst.get('z'))
    sst.put('l', 0)
    print('first: ', sst.first.key)
    print(sst.size())
    print(sst.key())






