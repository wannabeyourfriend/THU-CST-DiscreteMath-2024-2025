class Proposition:
    def __init__(self, name):
        self.name = name
        self.value = None

    def divide(self):
        return {self}

    def assign(self, values):
        self.value = values[self.name]

    def evaluate(self):
        return self.value


    def __eq__(self, other):
        if not isinstance(other, Proposition):
            return False
        return self.name == other.name

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(str(self))
  
class Not:
    def __init__(self, formula):
        self.formula = formula

    def divide(self):
        return self.formula.divide()

    def assign(self, values):
        self.formula.assign(values)

    def evaluate(self):
        return not self.formula.evaluate()


    def __eq__(self, other):
        if not isinstance(other, Not):
            return False
        return self.formula == other.formula

    def __str__(self):
        return '~' + str(self.formula)

    def __hash__(self):
        return hash(str(self))

class And:
    def __init__(self, formula_a, formula_b):
        self.formula_a = formula_a
        self.formula_b = formula_b

    def divide(self):
        return self.formula_a.divide() | self.formula_b.divide()

    def assign(self, values):
        self.formula_a.assign(values)
        self.formula_b.assign(values)

    def evaluate(self):
        return self.formula_a.evaluate() and self.formula_b.evaluate()

  
    def __eq__(self, other):
        if not isinstance(other, And):
            return False
        return self.formula_a == other.formula_a and \
               self.formula_b == other.formula_b

    def __str__(self):
        return '(%s /\\ %s)' % (self.formula_a, self.formula_b)

    def __hash__(self):
        return hash(str(self))

class Or:
    def __init__(self, formula_a, formula_b):
        self.formula_a = formula_a
        self.formula_b = formula_b

    def divide(self):
        return self.formula_a.divide() | self.formula_b.divide()

    def assign(self, values):
        self.formula_a.assign(values)
        self.formula_b.assign(values)

    def evaluate(self):
        return self.formula_a.evaluate() or self.formula_b.evaluate()


    def __eq__(self, other):
        if not isinstance(other, Or):
            return False
        return self.formula_a == other.formula_a and \
               self.formula_b == other.formula_b

    def __str__(self):
        return '(%s \\/ %s)' % (self.formula_a, self.formula_b)

    def __hash__(self):
        return hash(str(self))

class Implies:
    def __init__(self, formula_a, formula_b):
        self.formula_a = formula_a
        self.formula_b = formula_b

    def divide(self):
        return self.formula_a.divide() | self.formula_b.divide()

    def assign(self, values):
        self.formula_a.assign(values)
        self.formula_b.assign(values)

    def evaluate(self):
       return not self.formula_a.evaluate() or self.formula_b.evaluate()

    def __eq__(self, other):
        if not isinstance(other, Implies):
            return False
        return self.formula_a == other.formula_a and \
               self.formula_b == other.formula_b

    def __str__(self):
        return '(%s -> %s)' % (self.formula_a, self.formula_b)

    def __hash__(self):
        return hash(str(self))

class Equiv:
    def __init__(self, formula_a, formula_b):
        self.formula_a = formula_a
        self.formula_b = formula_b

    def divide(self):
        return self.formula_a.divide() | self.formula_b.divide()

    def assign(self, values):
        self.formula_a.assign(values)
        self.formula_b.assign(values)

    def evaluate(self):
        return self.formula_a.evaluate() == self.formula_b.evaluate()


    def __eq__(self, other):
        if not isinstance(other, Equiv):
            return False
        return self.formula_a == other.formula_a and \
               self.formula_b == other.formula_b

    def __str__(self):
        return '(%s <-> %s)' % (self.formula_a, self.formula_b)

    def __hash__(self):
        return hash(str(self))

class BoolConstant:
    def __init__(self, name):
        self.name = name
        if name == 'T':
            self.value = True
        elif name == 'F':
            self.value = False

    def divide(self):
        return {self}

    def assign(self, values):
        pass

    def evaluate(self):
        return self.value   

    def __eq__(self, other):
        if not isinstance(other, BoolConstant):
          return False
        return self.name == other.name

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(str(self))
