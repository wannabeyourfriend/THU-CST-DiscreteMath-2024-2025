import functools

class Relation(object):
    def __init__(self, sets, rel):
        assert not(len(sets)==0 and len(rel) > 0) #不允许sets为空而rel不为空
        assert sets.issuperset(set([x[0] for x in rel]) | set([x[1] for x in rel])) #不允许rel中出现非sets中的元素
        self.rel = rel
        self.sets = sets

    def __str__(self):
        relstr = '{}'
        setstr = '{}'
        if len(self.rel) > 0:
            relstr = str(self.rel)
        if len(self.sets) > 0:
            setstr = str(self.sets)
        return 'Relation: ' + relstr + ' on Set: ' + setstr

    def __eq__(self, other):
        return self.sets == other.sets and self.rel == other.rel

    def diagonalRelation(self):
        return Relation(self.sets, set([(a, a) for a in self.sets]))

    def inverse(self):
        # 计算关系的逆
        inverse_rel = set((b, a) for (a, b) in self.rel)
        return Relation(self.sets, inverse_rel)

    def __mul__(self, other):
        assert self.sets == other.sets
        return Relation(self.sets, set([(x, z) for (x, y1) in other.rel for (y2, z) in self.rel if y1 == y2]))

    def __pow__(self, power, modulo=None):
        assert power >= -1
        if power == -1:
            return self.inverse()
        if power == 0:
            return self.diagonalRelation()
        if power == 1:
            return self
        result = self
        for _ in range(1, power):
            result = result * self
        return result

    def __add__(self, other):
        return Relation(self.sets, self.rel | other.rel)

    def toMatrix(self):
        # my code：
        matrix = [[0] * len(self.sets) for _ in range(len(self.sets))]
        elems = sorted(list(self.sets))
        for elem in elems:
            rels_from_elem = [rel for rel in self.rel if rel[0] == elem]
            for rel in rels_from_elem:
                matrix[elems.index(elem)][elems.index(rel[1])] = 1
        return matrix
    # answer：
    """
    def toMatrix(self):
        #将序偶集合形式的关系转换为矩阵。
        #为保证矩阵的唯一性，需对self.sets中的元素先排序
        matrix = []
        elems = sorted(list(self.sets))
        line = [0]*len(self.sets)
        for elem in elems:
            #请在此处编写程序，实现转换为矩阵的功能
            tups = [x for x in self.rel if x[0] == elem]
            for item in tups:
                line[elems.index(item[1])] = 1
            matrix.append(line)
            line = [0]*len(self.sets)
            #请在上面编写程序，不要修改下面的代码
        return matrix
    """

    def isReflexive(self):
        # 判断self是否为自反关系，是则返回True，否则返回False
        if not self.rel:
            return True
        for item in self.sets:
            if (item, item) not in self.rel:
                return False
            else:
                continue
        return True
    """
    def isReflexive(self):
        # 判断self是否为自反关系，是则返回True，否则返回False
        # 请删除pass后编程实现该方法功能
        # pass
        for a in self.sets:
            if not ((a, a) in self.rel):
                return False
        return True
    """
    def isIrreflexive(self):
        # 判断self是否为反自反关系，是则返回True，否则返回False
        # 请删除pass后编程实现该方法功能
        for a in self.sets:
            if (a, a) in self.rel:
                return False
        return True

    def isSymmetric(self):
        # 判断self是否为对称关系，是则返回True，否则返回False
        if not self.rel:
            return True
        for rel in self.rel:
            reverse_rel = (rel[1], rel[0])
            if reverse_rel not in self.rel:
                return False
            else:
                continue
        return True

    def isAntiSymmetric(self):
        for (a, b) in self.rel:
            if (b, a) in self.rel:
                if a != b:
                    return False
        return True

    def isTransitive(self):
        for (a, b) in self.rel:
            for (b, c) in self.rel:
                if (a, c) not in self.rel:
                    return False
        return True

    def reflexiveClosure(self):
        return self + self.diagonalRelation()

    def symmetricClosure(self):
        symmetricClosure_rel = set(self.rel)
        for (a, b) in self.rel:
            symmetricClosure_rel.add((b, a))
        return Relation(self.sets, symmetricClosure_rel)

    def transitiveClosure(self):
        transitiveClosure_relation = set(self.rel)
        changed = True
        while changed:
            changed = False
            for (a, b) in self.rel:
                for (c, d) in self.rel:
                    if b == c and (a, d) not in transitiveClosure_relation:
                        transitiveClosure_relation.add((a, d))
                        changed = True
        return Relation(self.sets, transitiveClosure_relation)

    def __warshall(self, adj_matrix):
        assert (len(row) == len(adj_matrix) for row in adj_matrix)
        n = len(adj_matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj_matrix[i][j] = adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j])

        return adj_matrix
