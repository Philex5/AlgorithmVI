import numpy as np

class WeightedQuickUnionUF:
    """
    init初始化每一个触点以及它所属的连通分量
    union将两个触点的连通分量合并，表示它们互相连接
    find判定它所在的分量所需的信息保存在id[i]之中
    connected 实现触点相连
    count 统计分量的数量
    """

    def __init__(self, n):
        self.count = n
        self.ids = []
        self.sz = []  # 各个根节点所对应的分量的大小

        for i in range(n):
            self.ids.append(i)
        for j in range(n):
            self.sz.append(1)

    def find(self, p):
        while p != self.ids[p]:   # 根节点序号索引的值是它本身
            self.ids[p] = self.ids[self.ids[p]]  #路径压缩
            p = self.ids[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        qucik-union 列表里存的是链接而不是所属的分量，根节点互连
        """
        proot = self.find(p)
        qroot = self.find(q)

        if proot == qroot:
            return

        if self.sz[proot] > self.sz[qroot]:
            self.ids[qroot] = proot
            self.sz[proot] += self.sz[qroot]
        else:
            self.ids[proot] = qroot
            self.sz[qroot] += self.sz[proot]

        self.count -= 1


if __name__ == '__main__':
    a = np.array([[4, 3], [3, 8], [6, 5], [9, 4], [2, 1], [8, 9], [5, 0],[7, 2], [6, 1], [1, 0], [6, 7]])

    uf = WeightedQuickUnionUF(10)
    for i in range(len(a)):
        p = a[i][0]
        q = a[i][1]
        if(uf.connected(p, q)):
            continue
        uf.union(p, q)
        print('{} <-> {}'.format(p, q))

    print(uf.count)


