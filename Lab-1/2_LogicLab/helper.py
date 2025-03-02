from propParse import *
def formatFormula(form):
    #请在此编程实现函数功能
    correpond = {'/\\':' and ', '\\/':' or ', '->':' implies ', '~':' not ', '<->':' equiv '}
    for item in ['/\\', '\\/', '<->', '->', '~']:
        form = form.replace(item, correpond[item])
    return form.replace('  ', ' ').replace('( ', '(').replace(' )', ')')

def genInterpretations(n):
    from itertools import product
    # 生成所有可能的解释
    return [list(p) for p in product([False, True], repeat=n)]

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

