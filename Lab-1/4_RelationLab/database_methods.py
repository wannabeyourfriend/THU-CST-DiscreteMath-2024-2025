from reldatabase import RelDB
def defineTables():
    dept_attributes = ["DNO", "DNAME", "BUDGET"]
    dept_data = [
        {"DNO": "D1", "DNAME": "Marketing", "BUDGET": "10M"},
        {"DNO": "D2", "DNAME": "Development", "BUDGET": "12M"},
        {"DNO": "D3", "DNAME": "Research", "BUDGET": "5M"}
    ]
    dept = RelDB(dept_attributes, dept_data)

    # Creating the first employee table
    emp_attributes = ["ENO", "ENAME", "DNO", "SALARY"]
    emp_data = [
        {"ENO": "E1", "ENAME": "Lopez", "DNO": "D1", "SALARY": "40K"},
        {"ENO": "E2", "ENAME": "Cheng", "DNO": "D1", "SALARY": "42K"},
        {"ENO": "E3", "ENAME": "Finzi", "DNO": "D2", "SALARY": "30K"}
    ]
    emp = RelDB(emp_attributes, emp_data)

    # Creating the second employee table
    emp2_data = [
        {"ENO": "E3", "ENAME": "Finzi", "DNO": "D2", "SALARY": "30K"},
        {"ENO": "E4", "ENAME": "Saito", "DNO": "D2", "SALARY": "35K"}
    ]
    emp2 = RelDB(emp_attributes, emp2_data)

    return dept, emp, emp2

def project(orig_dict, attributes):
    return {attr: orig_dict[attr] for attr in attributes if attr in orig_dict}


def PROJECT(orig_rel, attributes):
    projected_data = [project(tup, attributes) for tup in orig_rel.tuples()]
    return RelDB(attributes, projected_data)

def SELECT(orig_rel, restriction):
    """
    从给定关系数据表中选择符合条件的元组。
    restriction是一个函数，接受一个字典（元组转换后的形式）并返回一个布尔值。
    """
    # 使用生成器表达式过滤符合条件的元组
    selected_tuples = (tup for tup in orig_rel.tuples() if restriction(tup))
    
    # 返回一个新的关系数据表，其中包含已选择的元组
    return RelDB(orig_rel.attributes(), selected_tuples)    

def JOIN(rel_1, rel_2):
    assert not(set(rel_1.attributes()) & set(rel_2.attributes()) == set())
    
    common_attrs = set(rel_1.attributes()) & set(rel_2.attributes())
    new_attrs = list(rel_1.attributes()) + [attr for attr in rel_2.attributes() if attr not in common_attrs]
    
    joined_tuples = set()
    for t1 in rel_1.tuples():
        for t2 in rel_2.tuples():
            if all(t1[attr] == t2[attr] for attr in common_attrs):
                new_tuple = tuple(t1[attr] for attr in rel_1.attributes()) + tuple(t2[attr] for attr in rel_2.attributes() if attr not in common_attrs)
                joined_tuples.add(new_tuple)
    
    return RelDB(new_attrs, joined_tuples)