from random import *


def findNomap(A, f):
    for a in A:
        mapped = False
        for m in f:
            if m[1] == a:
                mapped = True
                break
        if mapped == False:
            return a
    return None


def mapping(A, f):
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A
    unmapped_element = findNomap(A, f)
    if unmapped_element is not None:
        for m in f:
            if m[0] == unmapped_element:
                f.remove(m)
        A.remove(unmapped_element)
        return mapping(A, f)
    return A


def InsertSort(seq, i):
    if i <= 0:
        return

    InsertSort(seq, i - 1)

    key = seq[i]
    j = i - 1
    while j >= 0 and seq[j] > key:
        seq[j + 1] = seq[j]
        j -= 1
    seq[j + 1] = key


def SelectSort(seq, i):
    if i == 0:
        return

    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]:
            max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]

    SelectSort(seq, i - 1)


def QuickSort(seq):
    if len(seq) <= 1:
        return seq
    pivot = seq[len(seq) // 2]
    left = [x for x in seq if x < pivot]
    middle = [x for x in seq if x == pivot]
    right = [x for x in seq if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)


if __name__ == "__main__":
    f = [(1, 3), (2, 1), (3, 1), (4, 5), (5, 5), (6, 4), (7, 6)]
    g = [(1, 3), (3, 1), (4, 5), (6, 4), (5, 7), (7, 6)]
    h = [(1, 3), (3, 2), (4, 4), (6, 7), (2, 2), (7, 5)]
    for l in [f, g, h]:
        A = [1, 2, 3, 4, 5, 6, 7]
        print(mapping(A, l))

    print('*' * 20)

    seed(999)
    test = [[], [], [], []]
    for i in range(4):
        for j in range(10):
            test[i].append(randint(1, 100))

    for l in test:
        InsertSort(l, len(l) - 1)
        print(l)

    print('*' * 20)

    seed(9999)
    test1 = [[], [], [], []]
    for i in range(4):
        for j in range(10):
            test1[i].append(randint(100, 1000))

    for l in test1:
        SelectSort(l, len(l) - 1)
        print(l)

    print('*' * 20)
    seed(99999)
    test2 = [[], [], [], []]
    for i in range(4):
        for j in range(10):
            test2[i].append(randint(10, 1000))

    for l in test2:
        print(QuickSort(l))

