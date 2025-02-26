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

