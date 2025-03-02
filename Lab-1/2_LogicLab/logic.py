from pyparsing import (alphanums, alphas, delimitedList, Forward,oneOf,
            Group, Keyword, Literal, opAssoc, operatorPrecedence,
            ParserElement, ParseException, ParseSyntaxException, Suppress,ZeroOrMore,
            Word)

ParserElement.enablePackrat()
from proposition import *
##########################################################################
def propAction(tokens):
    return Proposition(tokens[0])

def notFormulaAction(tokens):
    return Not(tokens[0][1])

def boolConstantAction(tokens):
    return BoolConstant(tokens[0])

def andFormulaAction(tokens):
    return And(tokens[0][0], tokens[0][2])

def orFormulaAction(tokens):
    return Or(tokens[0][0], tokens[0][2])

def impliesFormulaAction(tokens):
    return Implies(tokens[0][0], tokens[0][2])

def equivFormulaAction(tokens):
    return Equiv(tokens[0][0], tokens[0][2])