from relation import Relation
def isEquivalenceRelation(rel):
    #该函数对给定的Relation对象rel，判断其是否为等价关系
    #是则返回True，否则返回False
    if rel.isReflexive() and rel.isSymmetric() and rel.isTransitive():
        return True
    else:
        return False

def find_equivalence_class(a, relation):
    eq_class = []
    for element in relation.sets:
        if (a, element) in relation.rel or (element, a) in relation.rel:
            eq_class.append(element)
    return eq_class

def createPartition(rel):
    #对给定的Relation对象rel，求其决定的rel.sets上的划分
    #如果rel不是等价关系，返回空集
    if not isEquivalenceRelation(rel):
        print("The given relation is not an Equivalence Relation")
        return set([])
    #如rel是等价关系，实现求划分的程序
    partitions =set()
    visited = set()
    for a in rel.sets:
        if a not in visited:
            eq_class = find_equivalence_class(a, rel)
            partitions.add(frozenset(eq_class))
            visited.add(a)
    return partitions


def createEquivalenceRelation(partition, A):
    # Ensure that the union of all subsets in the partition equals A
    assert functools.reduce(lambda x, y: x.union(y), partition) == A

    # Initialize the relation as an empty set
    relation = set()

    # Iterate over each subset in the partition
    for subset in partition:
        # For each pair of elements in the subset, add a relation
        for x in subset:
            for y in subset:
                relation.add((x, y))

    # Create a Relation object (assuming a Relation class definition is available)
    return Relation(relation, A)


def isPartialOrder(rel):
    return rel.isReflexive() and rel.isAntiSymmetric() and rel.isTransitive()

def isQuasiOrder(rel):
    # 该函数对给定的Relation对象rel，判断其是否为拟序关系
    # 是则返回True，否则返回False。
    if rel.isIrreflexive() and rel.isTransitive():
        return True
    else:
        return False

def isLinearOrder(rel):
    # 该函数对给定的Relation对象rel，判断其是否为全序关系
    #是则返回True，否则返回False
    if not isPartialOrder(rel):
        return False
    else:
        for x in rel.sets:
            for y in rel.sets:
                if (x, y) not in rel.rel and (y, x) not in rel.rel:
                    return False
    return True

def join(rel1, rel2):
    #对给定的关系rel1和rel2
    assert rel1.sets == rel2.sets
    M1 = rel1.toMatrix()
    M2 = rel2.toMatrix()

    m = len(M1)
    n = m
    M = []
    #实现关系矩阵的join运算，结果存于M中
    for i in range(m):
        row = []
        for j in range(n):
            row.append(M1[i][j] or M2[i][j])
        M.append(row)
    return M

def meet(rel1, rel2):
    # 对给定的关系rel1和rel2
    assert rel1.sets == rel2.sets
    M1 = rel1.toMatrix()
    M2 = rel2.toMatrix()
    m = len(M1)
    n = m
    M = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(M1[i][j] and M2[i][j])
        M.append(row)
    return M

def booleanProduct(rel1, rel2):
    # 对给定的关系rel1和rel2
    assert rel1.sets == rel2.sets

    # 首先得到二者的矩阵
    M1 = rel1.toMatrix()
    M2 = rel2.toMatrix()

    m = len(M1)
    n = m
    M = [[0] * n for _ in range(m)]
    #**********  Begin  **********#
    # 实现关系矩阵的布尔乘积运算，结果存于M中
    for i in range(m):
        row = []
        for j in range(n):
            temp = 0
            for k in range(n):
                temp = temp or (M1[i][k] and M2[k][j])
            row.append(temp)
        M.append(row)
    return M
