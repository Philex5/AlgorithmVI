class stack:
    def __init__(self, arr):
        self.arr = arr
        self.point = len(arr) -1

    def push(self, ele):
        self.arr.append(ele)
        self.point += 1
    def pop(self):
        if self.point < 0:
            print( 'Empty Stack !')
        self.point -= 1
        return self.arr.pop()


# 用栈实现简单的算术表达式的计算
def calc(expression):
    nums = stack([])
    opes = stack([])

    for ele in expression:
        if ele == '(':
            continue
        if ele == '+' or ele == '-' or ele == '*'\
                or ele == '/':
            opes.push(ele)
        elif ele == ')':
            ope = opes.pop()
            num = nums.pop()
            if ope == '+':
                num += nums.pop()
            elif ope == '-':
                num = nums.pop() - num
            elif ope == '*':
                num *= nums.pop()
            elif ope == '/':
                num = nums.pop() / num
            nums.push(num)
        else:
            nums.push(float(ele))
    return nums.pop()


if __name__ == '__main__':
    # s = stack([1, 2,  3, 4])
    # for i in range(4):
    #     print(s.pop())
    # for i in range(5):
    #     s.push(i*2)
    # print(s.point)
    # print(s.arr)
    expre = '((2+3)*(5/4))'
    print(calc(expre))


