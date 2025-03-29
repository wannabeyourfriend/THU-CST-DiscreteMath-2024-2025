class RelDB:
    """
    此为代表关系模型的类.
    RelDB用元组来保存关系数据表的表头（attributes_）,将输入为字典形式的
    数据表实际数据转换为元组后保存起来（tuples_），每一行数据的顺序与attributes_
    中的属性顺序一致，即用 attributes_来检索tuples_中的数据。
    """

    def __init__(self, attributes, dictset=set()):
        """
        用给定的attributes创建一个关系表.
        """
        self.attributes_ = tuple(attributes)
        self.tuples_ = set()
        self.tuples_.update(set([self._convert_dict(d) for d in dictset]))

    def __eq__(self, other):
        return self.attributes() == other.attributes() and self._tuples() == other._tuples()

    def __str__(self):
        return str(self.attributes_) + ' : ' + str(self.tuples_)

    def attributes(self):
        """
        返回self的成员attributes_.
        """
        return self.attributes_

    def _convert_dict(self, tup):
        """
        将输入的字典格式数据tup转换为内部的元组格式.
        """
        # 如果输入已经是元组对象，则不需要转换
        if isinstance(tup, tuple):
            return tup
        else:
            return tuple([tup[attribute] for attribute in self.attributes_])

    def add(self, tup=None, **kwargs):
        """
        将字典形式的数据tup或**kwargs格式的关系表数据以元组形式加入到关系表.
        """
        if tup is None:
            tup = kwargs
        self.tuples_.add(self._convert_dict(tup))

    def add_tuple(self, tup):
        """
        将元组形式的关系表数据tup加入到该关系表
        """
        self.tuples_.add(tup)

    def add_multiple(self, tupset):
        """
        将字典tupset中的数据批量加入为该关系数据表的数据
        """
        self.tuples_.update(set([self._convert_dict(tup) for tup in tupset]))

    def _tuples(self):
        return self.tuples_

    def tuples(self):
        """
        一个返回关系数据表中tuples_数据的生成器
        """
        for tup in self._tuples():
            yield dict(zip(self.attributes_, tup))

    def display(self):
        """
        显示该关系数据表
        """
        columns = range(len(self.attributes_))

        col_width = [len(self.attributes_[col]) for col in columns]

        for tupdict in self.tuples():
            tup = self._convert_dict(tupdict)
            for col in columns:
                col_width[col] = max(col_width[col], len(tup[col]))

        hline = ""
        for col in columns:
            hline += "+-" + ("-" * col_width[col]) + "-"
        hline += "+"

        def line(row):
            l = ""
            for col in columns:
                value = row[col]
                l += "| " + value + (" " * (col_width[col] - len(value))) + " "
            l += "|"
            return l

        print(hline)
        print(line(self.attributes_))
        print(hline)

        for tup in self.tuples():
            print(line(self._convert_dict(tup)))

        print(hline)
