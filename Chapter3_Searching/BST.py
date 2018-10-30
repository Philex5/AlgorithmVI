from collections import deque

# 基于二叉查找树的符号表


class Node:
    def __init__(self, key, value, node_num, left_node=None, right_node=None):
        self.key = key
        self.val = value
        self.node_num = node_num
        self.left = left_node
        self.right = right_node


class BST:
    def __init__(self, nodes):
        self.nodes = nodes
        self.root = nodes[0]

    # 整个二叉树的节点个数
    def size(self):
        return self.root.node_num

    # 以当前节点为根节点的树的节点个数
    def node_size(self, x):
        if x is None:
            return 0
        return x.node_num

    def get(self, key):
        return self.get_val(self.root, key)

    def get_val(self, node_key, key):
        if node_key is None:
            return
        if key == node_key.key:
            return node_key.val
        elif key > node_key.key:
            return self.get_val(node_key.right, key)
        else:
            return self.get_val(node_key.left, key)

    def put(self, key, val):
        self.put_key(self.root, key, val)

    def put_key(self, node_key, key, val):
        if node_key is None:
            return Node(key, val, 1)
        if key == node_key.key:
            node_key.val = val
        elif key > node_key.key:
            node_key.right = self.put_key(node_key.right, key, val)
        else:
            node_key.left = self.put_key(node_key.left, key, val)
        node_key.node_num = self.node_size(node_key.left) + self.node_size(node_key.right)+1
        return node_key

    def min(self, node):
        if node is None:
            return
        while node.left is not None:
            node = node.left
        return node.key

    def max(self, node):
        if node is None:
            return
        while node.right is not None:
            node = node.right
        return node.key

    """
    向上取整, 大于等于key的最小值
    若node_key键值等于key,那么就是node_key
    若node_key键值小于key, 那么肯定在右边
    若node_key键值大于key,那么可能就是node_key或者在左边
    
    """
    def ceiling(self, key):
        node = self.get_ceiling(self.root, key)
        if node is None:
            return None
        return node

    def get_ceiling(self, node_key, key):
        if node_key is None:
            return node_key
        if node_key.key == key:
            return node_key.key
        elif key > node_key.key:
            return self.get_ceiling(node_key.right, key)
        t = self.get_ceiling(node_key.left, key)
        if t is None:
            return node_key
        return t

    # 向下取整,小于等于key的最大数
    def floor(self, key):
        node = self.get_floor(self.root, key)
        if node is None:
            return None
        return node

    def get_floor(self, node_key, key):
        if node_key is None:
            return None
        if node_key.key == key:
            return node_key.key
        elif key < node_key.key:
            return self.get_floor(node_key.left, key)
        t = self.get_floor(node_key.right, key)
        if t is None:
            return node_key.key
        return t

    # 选择第k大的key值(从0开始算),即小于等于该key值的有k个键
    # 如果当前节点的左子节点的size
    def select(self, k):
        return self.select_k(self.root, k)

    def select_k(self, node_key, k):
        if node_key is None:
            return
        t = self.node_size(node_key.left)
        if t == k:
            return node_key.key
        elif t > k:
            return self.select_k(node_key.left, k)
        else:
            return self.select_k(node_key.right, k-t-1)

    def rank(self, key):
        return self.rank_key(self.root, key)

    def rank_key(self, node_key, key):
        if node_key is None:
            return 0
        elif node_key.key < key:
            return self.node_size(node_key.left) + 1 + self.rank_key(node_key.right, key)
        elif node_key.key > key:
            return self.rank_key(node_key.left, key)
        else:
            return self.node_size(node_key.left)

    """
    删除二叉查找树上的任意节点x
    1. 找出x后继节点l(右子树最小节点)
    2. l的左链接指向指向x的左链接t.left
    3. l的右链接指向x链接
    4. 指向x的链接指向l(递归实现)
    
    """
    def delete(self, key):
        self.root = self.deleteKey(self.root, key)

    def deleteKey(self, node_key, key):
        if node_key is None:
            return
        if node_key.key == key:
            if node_key.left is None:
                return node_key.right
            if node_key.right is None:
                return node_key.left
            new_node = self.min(node_key.right)
            new_node.left = node_key.left
            new_node.right = self.deleteMinkey(node_key.right)
            return new_node
        elif node_key.key > key:
            node_key.left = self.deleteKey(node_key.left, key)
        else:
            node_key.right = self.deleteKey(node_key.right, key)
        node_key.node_num = self.node_size(node_key.right) + self.node_size(node_key.left) + 1
        return node_key

    def deleteMinkey(self, node):
        if node is None:
            return
        temp = node
        while temp.left is not None:
            temp = temp.left
        temp.left = None
        return node

    def deleteMin(self):
        self.root = self.deleteMinKey(self.root)

    def deleteMinKey(self, node_key):
        if node_key.left is None:
            return node_key.right
        node_key.left = self.deleteMinKey(node_key.left)
        node_key.node_num = self.node_size(node_key.left) + self.node_size(node_key.right) + 1
        return node_key

    def deleteMax(self):
        self.root = self.deleteMaxKey(self.root)

    def deleteMaxKey(self, node_key):
        if node_key.right is None:
            return node_key.left
        node_key.right = self.deleteMaxKey(node_key.right)
        node_key.node_num = self.node_size(node_key.left) + self.node_size(node_key.right) + 1
        return node_key

    # 范围查找
    # 中序遍历
    def keys(self, low, high):
        queue = deque()
        self.findkeys(self.root, queue, low, high)
        return queue

    def findkeys(self, node_key, queue, low, high):
        if node_key is None:
            return
        if node_key.key > low:
            self.findkeys(node_key.left, queue, low, high)
        if low <= node_key.key <= high:
            queue.append(node_key.key)
        if node_key.key < high:
            self.findkeys(node_key.right, queue, low, high)


if __name__ == '__main__':
    root = Node('S', 0, 1)
    bst = BST([root])
    bst.put('E', 1)
    bst.put('A', 2)
    bst.put('R', 3)
    bst.put('C', 4)
    bst.put('A', 10)
    print(bst.size())
    print(bst.get('A'))
    print(bst.min(bst.root))
    print(bst.max(bst.root))
    print(bst.ceiling('C'))
    print(bst.floor('N'))
    print(bst.rank('M'))
    print(bst.select(3))
    # print(bst.min(bst.root))
    # bst.deleteMin()
    # print(bst.min(bst.root))
    # print(bst.max(bst.root))
    # bst.deleteMax()
    # print(bst.max(bst.root))
    # bst.delete('R')
    # bst.delete('A')
    # print(bst.size())
    print(bst.min(bst.root))
    print(bst.keys('A', 'S'))



