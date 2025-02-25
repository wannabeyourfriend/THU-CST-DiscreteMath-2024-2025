from random import *


# 第一题
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


# 请在下面编写代码
# **********  Begin  **********#

# **********  End  **********#
# 请不要修改下面的代码


# 第二题
def InsertSort(seq, i):


# 请在下面编写代码
# **********  Begin  **********#

# **********  End  **********#
# 请不要修改下面的代码


# 第三题
def SelectSort(seq, i):


# 请在下面编写代码
# **********  Begin  **********#

# **********  End  **********#

# 请不要修改下面的代码


# 第四题
def QuickSort(seq):


# 请在下面编写代码
# **********  Begin  **********#

# **********  End  **********#
# 请不要修改下面的代码


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

