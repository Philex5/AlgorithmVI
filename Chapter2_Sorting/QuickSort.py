import numpy as np

# 快速排序
def Quick(arr):
    low = 0
    high = len(arr) -1
    sort(arr, low, high)
    return arr


def sort(arr, low, high):
    if low >= high:
        return

    j = partition(arr, low, high)
    sort(arr, low, j-1)
    sort(arr, j+1, high)


def partition(arr, low, high):
    p_i = low
    p_j = high
    base = arr[low]
    while p_i < p_j:
        while arr[p_i] <= base and p_i < high:
            p_i += 1
        while arr[p_j] >= base and p_j > low:
            p_j -= 1
        if p_i < p_j:
            arr[p_i], arr[p_j] = arr[p_j], arr[p_i]
    arr[p_j], arr[low] = arr[low], arr[p_j]
    return p_j

# 三向切分的快速排序
def Quick3way(arr, low, high):
    if low >= high:
        return
    lt = low
    i = low+1
    gt = high
    v = arr[low]
    while i <= gt:
        if arr[i] < v:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1  # 让[lt, i]只有和v相等的值
            i += 1
        elif arr[i] > v:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1 # 相等值，[lt, i]间隔变大
    # low, a[low, lt-1] < v = a[lt, gt] < a[gt+1, high]
    Quick3way(arr, low, lt-1)
    Quick3way(arr, gt+1, high)
    return arr


if __name__ == '__main__':

    print(Quick([7, 12, 13, 2, 8, 9]))
    print(Quick3way([7, 12, 12, 4, 5, 6, 7,7, 5, 6, 6, 13, 4, 4, 4], 0, 14))