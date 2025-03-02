from pyparsing import (alphanums, alphas, delimitedList, Forward,oneOf,
            Group, Keyword, Literal, opAssoc, operatorPrecedence,
            ParserElement, ParseException, ParseSyntaxException, Suppress,ZeroOrMore,
            Word)

ParserElement.enablePackrat()

##########################################################################
def propAction(tokens):
    return Proposition(tokens[0])

def notFormulaAction(tokens):
    return Not(tokens[0][1])

def boolConstantAction(tokens):
    #请删除pass后编程
    #pass
    return BoolConstant(tokens[0])

def andFormulaAction(tokens):
    #请删除pass后编程
    #pass
    return And(tokens[0][0], tokens[0][2])

def orFormulaAction(tokens):
    #请删除pass后编程
    #pass
    return Or(tokens[0][0], tokens[0][2])

def impliesFormulaAction(tokens):
    #请删除pass后编程
    #pass
    return Implies(tokens[0][0], tokens[0][2])

def equivFormulaAction(tokens):
    #请删除pass后编程
    #pass
    return Equiv(tokens[0][0], tokens[0][2])

##########################################################################
def propParse(text):
    left_parenthesis = Literal('(').suppress()
    right_parenthesis = Literal(')').suppress()
    implies = Keyword("implies")
    equivalence = Keyword("equiv")
    or_ = Keyword("or")
    and_ = Keyword("and")
    not_ = Keyword("not")
    connective = and_ | or_ | implies | equivalence
    boolean = Keyword("F") | Keyword("T")
    proposition = Word(alphas[0:26].upper().replace('F', '').replace('T', '')).setParseAction(propAction)
    formula = Forward()

    connectiveFormula = Group(left_parenthesis + formula + connective + formula + right_parenthesis)
    notFormula = Group(not_ + formula)

    operand = proposition | connectiveFormula | boolean | notFormula

    formula << operatorPrecedence(operand, [
        (not_, 1, opAssoc.RIGHT, notFormulaAction),
        (and_, 2, opAssoc.LEFT, andFormulaAction),
        (or_, 2, opAssoc.LEFT, orFormulaAction),
        (implies, 2, opAssoc.LEFT, impliesFormulaAction),
        (equivalence, 2, opAssoc.LEFT, equivFormulaAction)])

    boolean.setParseAction(boolConstantAction)
    try:
        result = formula.parseString(text, parseAll=True)
        assert len(result) == 1
        return result[0]
    except (ParseException, ParseSyntaxException) as err:
        print("Syntax error:\n{0.line}\n{1}^".format(err,
                                                     " " * (err.column - 1)))
        return []

##########################################################################

class Proposition:
    def __init__(self, name):
        self.name = name
        self.value = None

    def divide(self):
        return {self}

    def assign(self, values):
        self.value = values[self.name]

    def evaluate(self):
        # 请删除下面的pass后完成函数功能
        # pass
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
        # 请删除下面的pass后完成函数功能
        # pass
        return not (self.formula.evaluate())

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
        # 请删除下面的pass后完成函数功能
        # pass
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
        # 请删除下面的pass后完成函数功能
        # pass
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
        # 请删除下面的pass后完成函数功能
        # pass
        return not (self.formula_a.evaluate()) or self.formula_b.evaluate()

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
        # 请删除下面的pass后完成函数功能
        # pass
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
        # 请删除下面的pass后完成函数功能
        # pass
        return self.value

    def __eq__(self, other):
        if not isinstance(other, BoolConstant):
          return False
        return self.name == other.name

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(str(self))

################################################################
def formatFormula(form):
    correpond = {'/\\': ' and ', '\\/': ' or ', '->': ' implies ', '~': ' not ', '<->': ' equiv '}
    for item in ['/\\', '\\/', '<->', '->', '~']:
        form = form.replace(item, correpond[item])
    return form


def genInterpretations(n):
    if n < 1:
        return [[]]
    subtable = genInterpretations(n - 1)
    return [row + [v] for row in subtable for v in [False, True]]


def genTruthTable(formula):
    #编译所给的命题逻辑公式；
    form = propParse(formatFormula(formula))
    #获得该命题逻辑公式的所有命题词；
    propSet = form.divide()
    props = []
    for item in propSet:
        props.append(item.name)
    #对所有的命题词按照其名字的字典序排序
    props = sorted(props)
    #按照命题词个数，生成全部的解释；
    table = genInterpretations(len(props))

    #生成真值表的每一行数据
    for item in table:
        values = {}
        i = 0
        for prop in props:
            values[prop] = item[i]
            i += 1
        form.assign(values)
        result = form.evaluate()
        item.append(result)



    #显示真值表
    display(props, formula, table)


def display(props, formula, table):
    props.append(formula)
    columns = range(len(table[0]))
    col_width = [len(prop) for prop in props]
    symbol = {True: 'T', False: 'F'}

    hline = ""
    for col in columns:
        hline += "+-" + ("-" * col_width[col]) + "-"
    hline += "+"

    def line(row):
        l = ""
        for col in columns:
            if row[col] == True or row[col] == False:
                value = symbol[row[col]]
            else:
                value = row[col]

            if (col_width[col] - len(value)) % 2 == 0:
                l += "| " + (" " * ((col_width[col] - len(value)) // 2)) + value + (
                            " " * ((col_width[col] - len(value)) // 2)) + " "
            else:
                l += "| " + (" " * ((col_width[col] - len(value)) // 2 + 1)) + value + (
                            " " * ((col_width[col] - len(value)) // 2)) + " "
        l += "|"
        return l

    print(hline)
    print(line(props))
    print(hline)

    for onerow in table:
        print(line(onerow))

    print(hline)

def main():
    formula = '((P /\ R) /\ ~Q)'
    genTruthTable(formula)
    
main()