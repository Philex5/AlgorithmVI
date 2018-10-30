import numpy as np


class UF:
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
        for i in range(n):
            self.ids.append(i)


    def find(self, p):
        return self.ids[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        qucik-find: 合并p,q所在的连通分量，将两个触点所在的分量中的触点的值改为相同
        """
        idp = self.find(p)
        idq = self.find(q)

        if (idp == idq): return

        for i in range(len(self.ids)):
            if (self.ids[i] == idp):
                self.ids[i] = idq
        self.count -= 1

if  __name__ == '__main__':
    a = np.array([[4, 3], [3, 8], [6, 5], [9, 4], [2, 1], [8, 9], [5, 0],[7, 2], [6, 1], [1, 0], [6, 7]])

    uf = UF(10)
    for i in range(len(a)):
        p = a[i][0]
        q = a[i][1]
        if(uf.connected(p, q)):
            continue
        uf.union(p, q)
        print('{} <-> {}'.format(p, q))

    print(uf.count)


