def sink(a, k, N):
    while k * 2 <= N:
        j = k * 2
        if j < N and (a[j] < a[j+1]):
            j += 1
        if a[k] > a[j]:
            break
        a[k], a[j] = a[j], a[k]
        k = j


def HeapSort(a):
    N = len(a)-1
    k = N // 2
    # create_Heaps
    while k >= 1:
        sink(a, k, N)
        k -= 1
    print('Heap:', a)
    # HeapSort
    while N >= 1:
        a[1], a[N] = a[N], a[1]
        N -= 1
        sink(a, 1, N)
    print('Sorted_Heap:', a)


arr = [0, 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
HeapSort(arr)

