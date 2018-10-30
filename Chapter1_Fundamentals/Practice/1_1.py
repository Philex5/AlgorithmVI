import numpy as np
from Utils import swap


# Ndarray Transpose
def mytranpose(a):
    l,w = np.shape(a)
    for i in range(l):
        for j in range(i+1, w):
            a[i, j], a[j, i] = swap(a[i, j], a[j, i])

    print(a)

# Euclidean Maimum common divisor
def Euclidean(p, q):

    if p < q:
        p, q = swap(p, q)
    if p % q == 0:
        return q
    try:
        while(p%q != 0):
            r = p // q
            p = q
            q = r
    except ZeroDivisionError as e:
        print(e)

    return (p//q)



if __name__ == '__main__':

    a_t = mytranpose(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

    print(Euclidean(20, 6))



