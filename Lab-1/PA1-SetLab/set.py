def readAndPrintUniqueWords(filename):
    infile = open(filename, 'r')
    word_set = set()
    for line in infile:
        for word in line.split():
            if word not in word_set:
                print(word)
                word_set.add(word)
    infile.close()

def shakeSpeare(filename):
    fileline = open(filename,'r')
    words_set = set()
    for line in fileline:
        for word in line.split():
            if len(word)>=5:
                words_set.add(word)
    reverse = set()
    for word in words_set:
        reversed_word = word[::-1]
        if reversed_word in words_set:
            reverse.add(word)
            reverse.add(reversed_word)
    return reverse

def powSet(S):
    """
    powSet({1,2})的返回结果将为{frozenset(), frozenset({2}), frozenset({1}), frozenset({1, 2})}。
    采用递归的方式完成这道题目
    """
    if not S:
        return {frozenset()}
    element = S.pop()
    subsets = powSet(S)
    new_subsets = {subset | frozenset([element]) for subset in subsets}
    return subsets | new_subsets

def DescartesProduct(*args):
    a = []
    for s in args:
        a.append([x for x in s])
    a = DescartesProduct2([], a)
    b = set()
    for i in a:
        b.add(tuple(i))
    return b

def DescartesProduct2(list1, list2):
    if len(list2) == 0:
        return list1
    if len(list1) == 0:
        for x in list2[0]:
            list1.append([x])
        return DescartesProduct2(list1, list2[1:])
    nlist = []
    for i in list2[0]:
        for x in list1:
            a = [j for j in x]
            a.append(i)
            nlist.append(a)
    return DescartesProduct2(nlist, list2[1:])