RED = True
BLACK = False


class Node:
    def __init__(self, key, val, node_num, color, node_left=None, node_right=None):
        self.key = key
        self.val = val
        self.left = node_left
        self.right = node_right
        self.node_num = node_num
        self.color = color


class RedBlackTree:
    def __init__(self, nodes):
        self.nodes = nodes
        self.root = nodes[0]

    def isRed(self, node_key):
        if node_key is None:
            return False
        return node_key.color == RED

    def size(self):
        return self.root.node_num

    def isEmpty(self):
        return self.size == 0

    # 以当前节点为根节点的树的节点个数
    def node_size(self, x):
        if x is None:
            return 0
        return x.node_num

    def rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        x.node_num = h.node_num
        h.node_num = self.node_size(h.right) + self.node_size(h.left) + 1
        return x

    def rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        x.node_num = h.node_num
        h.node_num = self.node_size(h.right) + self.node_size(h.left) + 1
        return x

    def flipColor(self, h):
        h.color = RED
        h.right.color = BLACK
        h.left.color = BLACK

    # 红黑树插入操作
    def put(self, key, value):
        self.root = self.put_node(self.root, key, value)
        self.root.color = BLACK

    def put_node(self, h, key, value):
        if h is None:
            return Node(key, value, 1, RED)

        if key > h.key:
            h.right = self.put_node(h.right, key, value)
        elif key < h.key:
            h.left = self.put_node(h.left, key, value)
        else:
            h.value = value

        # 保证红链接全部为左链接
        if self.isRed(h.right) and not self.isRed(h.left):
            h = self.rotateLeft(h)
        # 4-节点右旋转
        if self.isRed(h.left) and self.isRed(h.left.left):
            h = self.rotateRight(h)
        if self.isRed(h.left) and self.isRed(h.right):
            self.flipColor(h)
        h.node_num = self.node_size(h.left) + self.node_size(h.right) + 1

        return h

    # 删除最小键,最小键肯定在最左边,沿着最左的路径向下即可,主要解决删除后填空的问题
    # 解决方案是保证所在的左节点不为2-节点,这样不会出现空节点,直接用该节点的后继节点替代
    def delete_flipcolor(self, h):  # 生成4-节点
        h.color = BLACK
        h.left.color = RED
        h.right.color = RED

    def moveRedLeft(self,  h):
        """
        假设节点h为红色，h.left和h.right 都是黑色
        将h.left或者h.left的子节点之一变红
        """
        self.delete_flipcolor(h)
        if self.isRed(h.right.left):
            h.right = self.rotateRight(h.right)
            h = self.rotateLeft(h)
        return h

    def balance(self, h):
        # 允许4-节点临时存在,删除完节点之后,向上返回会旋转配平
        if self.isRed(h.right):
            h = self.rotateLeft(h)
        # 保证红链接全部为左链接
        if self.isRed(h.right) and not self.isRed(h.left):
            h = self.rotateLeft(h)
        # 4-节点右旋转
        if self.isRed(h.left) and self.isRed(h.left.left):
            h = self.rotateRight(h)
        if self.isRed(h.left) and self.isRed(h.right):
            self.delete_flipcolor(h)
        h.node_num = self.node_size(h.left) + self.node_size(h.right) + 1

        return h

    def deleteMin(self):
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = RED
        self.root = self.deleteMin_Node(self.root)
        if not self.isEmpty():
            self.root.color = BLACK

    def deleteMin_Node(self, h):
        if h.left is None:
            return None
        # 不允许存在 2-节点,删完没得填,保证删除后节点不消失,这样后面可以向上分解所有的临时4-节点
        if not self.isRed(h.left) and not self.isRed(h.left.left):
            h = self.moveRedLeft(h)
        h.left = self.deleteMin_Node(h.left)
        return self.balance(h)

    # 删除最大键
    def moveRedRight(self, h):
        self.delete_flipcolor(h)
        if self.isRed(h.left.left):
            h = self.rotateRight(h)
        return h

    def deleteMax(self):
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = RED
        self.root = self.deleteMax_node(self.root)
        if not self.isEmpty():
            self.root.color = BLACK

    def deleteMax_node(self, h):
        if self.isRed(h.left):
            h = self.rotateRight(h)
        if h.right is None:
            return None
        if not self.isRed(h.right) and not self.isRed(h.right.left):
            h = self.moveRedRight(h)
        h.right = self.deleteMax_node(h.right)
        return self.balance(h)


   # 删除任意键
    def delete(self, key):
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = RED
        self.root = self.deleteNode(self.root, key)

    def deleteNode(self, h, key):
        if key < h.key:
            if not self.isRed(h.left) and not self.isRed(h.left.left):
                h = self.moveRedLeft(h)
            h.left = self.deleteNode(h.left, key)
        else:
            if self.isRed(h.left):
                h = self.rotateRight(h)
            if h.right is None and h.key == key:
                return None
            if not self.isRed(h.right) and not self.isRed(h.right.left):
                h = self.moveRedRight(h)
            if key == h.key:
                h.val = self.get(h.right, self.min(h.right).key)


if __name__ == '__main__':
    root = Node('S', 0, 1, BLACK)
    bst = RedBlackTree([root])
    bst.put('E', 1)
    bst.put('A', 2)
    bst.put('R', 3)
    bst.put('C', 4)
    bst.put('A', 10)
    print(bst.size())
    bst.deleteMax()
    print(bst.size())










