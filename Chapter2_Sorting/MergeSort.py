from copy import copy

# 原地归并算法
def MergeSort1(arr, low, mid, high):
    arr_x = copy(arr)
    i = low
    j = mid+1
    k = low

    while k <= high :
        if i > mid:
            arr[k] = arr_x[j]
            j += 1
            k += 1
        elif j > high:
            arr[k] = arr_x[i]
            i += 1
            k += 1
        elif arr_x[i] < arr_x[j]:
            arr[k] = arr_x[i]
            k += 1
            i += 1
        else:
            arr[k] = arr_x[j]
            k += 1
            j += 1

    return arr

# 自顶向下的归并排序： 递归实现
# 先归并大的数组
def MergeSort2(arr):
    low = 0
    high = len(arr) -1
    sort(arr, low, high)
    return arr


def sort(arr, low, high):
    if low >= high:
        return
    mid = low + (high-low) // 2
    sort(arr, low, mid)
    sort(arr, mid+1, high)
    MergeSort1(arr, low, mid, high)


# 自底向上的归并排序：
# 先归并小的数组
def MergeSort3(arr):
    l = len(arr)
    low = 0
    sz = 1
    while sz < l:
        low = 0
        while low < l-sz:
            MergeSort1(arr, low, low+sz-1, min(low+sz+sz-1, l-1))
            low += sz
        sz += sz
    return arr

if __name__ == '__main__':
    arr = [7, 12, 13, 2, 8, 9]
    #print(MergeSort1(arr, 0, 2, 5))
    print(MergeSort3(arr))