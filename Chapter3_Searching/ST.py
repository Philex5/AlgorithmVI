# 有序符号表API
class ST:
    # 创建一张有符号表（字典）
    def __init__(self, dict):
        self.st = dict

    # 将键值对存入表中（若值为空则将键key从表中删除)
    def put(self, key, val):
        if val == ' ':
            return
        self.st[key] = val

    # 获取键key对应的值(若键key不存在则返回空)
    def get(self, key):
        return self.st[key]

    # 从表中删除键key及其对应的值
    def delete(self, key):
        del self.st[key]

    # 键key是否存在于表中
    def contains(self, key):
        return key in self.st

    # 表是否为空
    def isEmpty(self):
        return self.size() == 0

    # 表中键值对的数量
    def size(self):
        return len(self.st.keys())

    # 最小的键
    def min(self):
        sorted_keys = self.sort_keys()
        return sorted_keys[0]

    # 最大的键
    def max(self):
        sorted_keys = self.sort_keys()
        return  sorted_keys[-1]

    # 小于等于key的最大键
    def floor(self, key):
        return self.keys(self.sort_keys()[0], key)[-1]

    # 大于等于key的最小键
    def ceiling(self, key):
        return self.keys(key, self.sort_keys()[-1])[0]

    # 小于key的键的数量
    def rank(self, key):
        return self.size_between(self.sort_keys()[0], key)

    # 排名为k的键
    def select(self, k):
        sorted_keys = self.sort_keys()
        return sorted_keys[k]

    # 删除最小的键
    def deleteMin(self):
        min_key = self.min()
        del self.st[min_key]

    # 删除最大的键
    def deleteMax(self):
        max_key = self.max()
        del self.st[max_key]

    # [low, high]之间的键的数量
    def size_between(self, low, high):
        selected_keys = self.keys(low, high)
        return len(selected_keys)

    # [low, high]之间的所有键，已排序
    def keys(self, low, high):
        if low > high:
            print('low < high')
            return
        sorted_keys = self.sort_keys()
        i = 0
        j = len(sorted_keys) - 1
        while sorted_keys[i] < low:
            i += 1
        while sorted_keys[j] > high:
            j -= 1

        return sorted_keys[i:j+1]

    # 表中所有键的集合,已排序
    def sort_keys(self):
        sorted_keys = sorted(self.st.keys())
        return sorted_keys


# dict = {'s': 1, 't': 2, 'a': 3, 'g': 4, 'z': 5}
# table = ST(dict)
# table.put('m', 6)
# print(table.st)
# print(table.get('z'))
#
# print(table.sort_keys())
# print(table.floor('b'))
# print(table.ceiling('l'))
# print(table.select(4))
# print(table.rank('y'))
# print(table.size())
# print(table.size_between('b', 'y'))
# print(table.contains('c'))
# print(table.contains('s'))
# print(table.keys('a', 'n'))
#
# print(table.max())
# table.deleteMax()
# print(table.min())
# table.deleteMin()
# print(table.st)
# print(table.isEmpty())
# table.st.clear()
# print(table.isEmpty())



