# Lab-1

[TOC]

## setLab

### Set 简介

Python提供了两种数据类型来建模数学中的集合：

- `set`：这是一个`mutable`非标量数据类型，用无序的方式组织一组有限的、可区分的、`immutable`（`hashable`）对象。
- `frozenset`：这是一个`immutable`、`hashable`的非标量数据类型，用无序的方式组织一组有限的、可区分的、`immutable`（`hashable`）对象。

- Python提供了预定义函数将任一迭代对象，如List、Tuple、Dictionary对象转换为一个Set对象:```set(iterable)```

- 集合可以用列表推导式创建，可以用来去除重复元素，还可以在for循环里面迭代集合元素

注意！`set`的元素不可以是`set`,但可以是`frozenset`

`set`上的方法有：

![预览大图](https://data.educoder.net/api/attachments/enh2UkQ4ZzF5KzFFZklyeWwzelIzUT09)

![预览大图](https://data.educoder.net/api/attachments/aUhqK3BGUTBBT2xOdUQvcXkyemNOZz09)

![预览大图](https://data.educoder.net/api/attachments/Z1B3S0NKUWdiTlNtU29OcXhGQit2Zz09)

![预览大图](https://data.educoder.net/api/attachments/MFlEY3pOeDA1Rm9qQ0s5Uk5QQTdWUT09)

### Set 底层实现

In Python Sets are implemented using a dictionary with dummy variables, where key beings the members set with greater optimizations to the time complexity.

| 1                                                            | 2                                                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![Lightbox](https://media.geeksforgeeks.org/wp-content/uploads/20250204154925405503/HashTable-300x278.png) | ![Lightbox](https://media.geeksforgeeks.org/wp-content/uploads/20250204154947769989/Hasing-Python.png) |

|             Operation             |     Average case      |                  Worst Case                   |                   notes                    |
| :-------------------------------: | :-------------------: | :-------------------------------------------: | :----------------------------------------: |
|              x in s               |         O(1)          |                     O(n)                      |                                            |
|            Union s\|t             |   O(len(s)+len(t))    |                                               |                                            |
|         Intersection s&t          | O(min(len(s), len(t)) |              O(len(s) * len(t))               | replace “min” with “max” if t is not a set |
| Multiple intersection s1&s2&..&sn |                       | (n-1)*O(l) where l is max(len(s1),..,len(sn)) |                                            |
|          Difference s-t           |       O(len(s))       |                                               |                                            |

|  Operators   |                      Notes                       |
| :----------: | :----------------------------------------------: |
|   key in s   |                containment check                 |
| key not in s |              non-containment check               |
|   s1 == s2   |              s1 is equivalent to s2              |
|   s1 != s2   |            s1 is not equivalent to s2            |
|   s1 <= s2   |                s1 is subset of s2                |
|   s1 < s2    |            s1 is proper subset of s2             |
|   s1 >= s2   |               s1 is superset of s2               |
|   s1 > s2    |           s1 is proper superset of s2            |
|   s1 \| s2   |              the union of s1 and s2              |
|   s1 & s2    |          the intersection of s1 and s2           |
|   s1 – s2    |       the set of elements in s1 but not s2       |
|   s1 ˆ s2    | the set of elements in precisely one of s1 or s2 |

### Set 较难题

> PA1-T3:实现幂集

```python
def powSet(S):
    if not S:
        return {frozenset()}
    element = S.pop()
    subsets = powSet(S)
    new_subsets = {subset | frozenset([element]) for subset in subsets}
    return subsets | new_subsets
```

> PA1-T4: 实现n个有限集合的笛卡尔乘积

```python
"""
# 偷鸡掉包
from itertools import product

def DescartesProduct(*args):
    # 使用 itertools.product 计算笛卡尔积
    return set(product(*args))
"""
def DescartesProduct(*args):
    a = []
    for s in args:
        a.append([x for x in s])
    a = DescartesProduct2([], a)
    b = set()
    for i in a:
        b.add(tuple(i))  
    return b

def DescartesProduct2(list1, list2):
    if len(list2) == 0:
        return list1
    if len(list1) == 0:
        for x in list2[0]:
            list1.append([x])  
        return DescartesProduct2(list1, list2[1:]) 
    nlist = []
    for i in list2[0]:
        for x in list1:
            a = [j for j in x]
            a.append(i)  
            nlist.append(a)
    return DescartesProduct2(nlist, list2[1:]) 
```

