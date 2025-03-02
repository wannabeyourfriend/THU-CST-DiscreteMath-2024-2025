from pyparsing import *
from proposition import *
from logic import *
"""
FOL BNF
    FORMULA     ::= PROPOSITION
                 |  '(' FORMULA CONNECTIVE FORMULA ')'
                 |  'not' FORMULA
                 |  '(' FORMULA ')'
                 |  'T'
                 |  'F'
    CONNECTIVE  ::= 'implies' | 'equiv' | 'and' | 'or'
    PROPOSITION ::= [A-Z]\w
"""
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
