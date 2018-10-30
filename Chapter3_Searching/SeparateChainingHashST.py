from Chapter3_Searching.SequentialSearchST import SequentialSearchSt
import numpy as np


# 基于拉链法的符号表
class SeparateChainingHashST:
    def __init__(self, N, M=997):
        self.N = N       # 键值对总数
        self.M = M       # 链表数量
        self.SequentialSearchSTs = []
        for i in range(M):
            self.SequentialSearchSTs.append(SequentialSearchSt())

    # 获取键key对应hash值, &操作是去除符号
    def hash(self, key):
        return (hash(key) & 0x7fffffff) % self.M

    # 获取键key对应的值
    def get_value(self,key):
        return self.SequentialSearchSTs[self.hash(key)].get(key)

    # 插入键值对
    def put(self, key, value):
        self.SequentialSearchSTs[self.hash(key)].put(key, value)

    # 删除指定键值对
    def delete(self, key):
        self.SequentialSearchSTs[self.hash(key)].delete(key)

    def Iterable(self):
        pass


# 基于线性探测法的符号表
class LinearProbingHashST:
    def __init__(self, M):
        self.N = 0  # 键值对总数
        self.M = 16  # 线性探测表的大小
        self.keys = [None] * self.M  # 键集合
        self.values = [None] * self.M  # 值集合

    def hash(self, key):
        return (hash(key) & 0x7fffffff) % self.M

    # 修改线性探测表的长度
    # 不能直接遍历赋值过去,需要重新计算位置插入
    def resize(self, length):
        t = LinearProbingHashST(length)
        for i in range(self.M):
            t.put(self.keys[i], self.values[i])
        self.keys = t.keys()
        self.values = t.values
        self.M = length

    def put(self, key, value):
        # 碰撞发生时, 将键值对放置到下一个索引的位置
        if self.N > self.M // 2:
            self.resize(self.M * 2)
        i = self.hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                self.values[i] = value
                return
            i = (i + 1) % self.M
        self.keys[i] = key
        self.values[i] = value
        self.N += 1

    def get(self, key):
        i = self.hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return self.values[i]
            i = (i + 1) % self.M
        return None

    # 线性探测法的删除不能直接把对应位置的值变为0或空,这样会使得之后位置的因碰撞而后移的key无法被找到,
    # 解决方案是把之后的键值对重新插入
    def delete(self, key):
        if not self.keys.__contains__(key):
            return
        i = self.hash(key)
        while self.keys[i] != key:
            i = (i + 1) % self.M
        self.keys[i] = None
        self.values[i] = None
        i = (i + 1) % self.M
        while self.keys[i] is not None:
            key_temp = self.keys[i]
            value_temp = self.values[i]
            self.keys[i] = None
            self.values[i] = None
            self.N -= 1
            self.put(key_temp, value_temp)
            i = (i + 1) % self.M
        self.N -= 1
        # 保证散列表的使用率在1/8-1/2之间
        if self.N > 0 and self.N == self.M // 8:
            self.resize(self.M // 2)
















