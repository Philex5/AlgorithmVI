import numpy as np
from random import randint
# 选择排序，不断选择剩余元素中最小者
def Selection(arr):
    l = len(arr)
    for i in range(l):
        iter_p = i
        for j in range(i+1, l):
            if arr[j] > arr[iter_p]:
                iter_p = j
        arr[iter_p], arr[i] = arr[i], arr[iter_p]


def Bubble_Sort(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)



# 插入排序：每一步将一个待排序的元素插入到前面排好序的数组之中
def Insertion(arr):
    l = len(arr)
    for i in range(l):
        j = i
        while j> 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


# 希尔排序： 对插入排序的改进，可以实现不相邻元素的互换
def Shell(arr):
    l = len(arr)
    h = l // 2
    while h >=1:
        for i in range(0, l, h):
            for j in range(i, 0, -h):
                if arr[j] < arr[j-h]:
                    arr[j], arr[j-h] = arr[j-h], arr[j]
        h = h // 2



if __name__ == '__main__':
    #Selection_Sort([3, 5, 1, 2, 7])
    Bubble_Sort([3, 5, 1, 2, 7])


