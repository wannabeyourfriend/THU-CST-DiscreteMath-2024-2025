class NaturalNumber(object):
    def __init__(self, pre):
        self.pre = pre

    def __str__(self):
        # 该方法在NaturalNumber对象被print时被调用
        # 请在下面编程
        result = ''
        if self.pre == None:
            result = "Zero"
        elif self.pre.pre == None:
            result = "Succ Zero"
        else:
            pre = self.pre
            result = "Succ(" + pre.__str__() + ")"
        return result

    def __add__(self, other):
        # 该方法重载了+运算，请编程实现自然数系统的加法：
        # a + zero = a
        # a + succ(b) = succ(a + b)
        if other.pre == None:
            return self
        else:
            return NaturalNumber(self + other.pre)

    def __mul__(self, other):
        # 该方法重载了+运算，请编程实现自然数系统的加法：
        # a * zero = zero
        # a * succ(b) =  a * b + a
        if other.pre == None:
            return NaturalNumber(None)
        else:
            return self * other.pre + self

    def toNumber(self):
        # 该方法实现NatrualNumber到其对应的阿拉伯数字的转换
        # 如zero->0, one->1，...
        if self.pre == None:
            return 0
        else:
            return self.pre.toNumber() + 1


def succ(n):
    # 返回一个以NaturalNumber对象n为前继的NaturalNumber对象
    return NaturalNumber(n)


def foldn(init, h, n):
    # 请在此处实现foldn的功能
    if n == 0:
        return init
    else:
        return h(foldn(init, h, n - 1))


def foldn2(init, h):
    def f(n: NaturalNumber):
        if n.pre is None:
            return init
        else:
            return h(foldn2(init, h)(n.pre))
    return f

