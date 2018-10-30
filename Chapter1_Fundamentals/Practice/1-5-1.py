import numpy as np


class UF:
    def __init__(self, n):
        self.count = n
        self.ids = []
        for i in range(n):
            self.ids.append(i)
        self.visit = 0  # 访问次数计数


    def find(self, p):
        self.visit += 1
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
            self.visit += 1
            if (self.ids[i] == idp):
                self.ids[i] = idq
                self.visit += 1
        self.count -= 1


a = np.array([[9, 0], [3, 4], [5, 8], [7, 2], [2, 1], [5, 7], [0, 3], [4, 2]])

uf = UF(10)
for i in range(len(a)):
    p = a[i][0]
    q = a[i][1]
    if(uf.connected(p, q)):
        continue
    uf.union(p, q)
    print('{} <-> {}'.format(p, q))
    print(uf.ids)
    print(uf.visit)

print(uf.count)

