# Lab-1

> 离散数学(1)-数理逻辑与集合论`头歌实践教学平台-离散数学实验-国防科大`

[TOC]

- 集合论 - **BoolLab**
  - 集合表示、性质、运算
  - 自然数
- 关系 - **RelationLab** 
  - 定义、运算
  - 闭包
- 数理逻辑 - **LogicLab**
  - 命题逻辑
  - 一阶谓词逻辑
- 布尔运算 - **BoolLab**
  - 真值表
  - 布尔代数
  - 电路模拟



## **1 setLab**

setlab包括两个实验，代码实现在`number.py`和`set.py`两个文件中

### 1.1 Set

#### Set 简介

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

#### Set 底层实现

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

#### Set 较难题

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

### 2.2 number

#### $N $的构造

Peano公理（又称佩亚诺公理）是一组定义自然数及其基本性质的公理系统，通常用于构建算术的基础。它由意大利数学家Giuseppe Peano在1889年提出。Peano公理的目的是从一些最基本的假设出发，推导出自然数的所有性质。

1.零是一个自然数： 0 是自然数。
2.每个自然数都有一个后继数： 对于每个自然数n，都有一个唯一的后继数（记作 S(n)）。
3.零不是任何自然数的后继数： 0 不是任何自然数的后继数。
4.后继数是唯一的： 如果两个自然数的后继数相同，那么这两个自然数本身是相同的。
5.归纳原理： 如果某个属性对于0成立，并且假设它对一个自然数n成立时，它对n的后继数S(n)也成立，那么这个属性对于所有自然数都成立。

这些公理构建了自然数的基本性质，如加法和乘法等操作都可以通过这些公理推导出来。

对于任意的集合 $A$, 定义$A^{+} = A \cup \{A\}$为集合$A$的后继.集合$0 = \emptyset$是一个自然数.根据这个定义，可以得到各个自然数：
$$
0 = \emptyset\\
1 =0^+ = 0 \cup \{0\} = \{0\}\\
2 = 1^+ = 1 \cup {1} = \{0,1\}\\
\cdots
$$
使用如下代码构造自然数

```python
class NaturalNumber(object):
    def __init__(self, pre):
        self.pre = pre
```

在代码中实现了自然数的输出、加法、乘法、形式化转换为数字等operation

#### $\mathbb{N} $同构列的构造

实际上，自然数还可以用函数来定义：$n=foldn(zero,succ,n)$,我们称foldn是自然数域上的叠加操作，其中succ是自然数上的函数，n是叠加的次数

- 函数式编程：

  > 在`foldn`函数的基础上，我们进一步定义`f(n)=foldn2(init,h)(n)`

![image-20250225193504497](C:\Users\35551\AppData\Roaming\Typora\typora-user-images\image-20250225193504497.png)

典型的函数式编程实现

```python
def foldn2(init, h):
    def f(n: NaturalNumber):
        if n.pre is None:
            return init
        else:
            return h(foldn2(init, h)(n.pre))
    return f
```

## **2 functionLab**

- **总结较难PA的思路**

> 实验背景:这个算法的背景和基本思想涉及集合和映射，特别是与固定点、不动点和自映射相关的概念。具体来说，你提到的映射 f 是从集合 A 到集合 A 的函数，即 f: A → A。算法的目标似乎是在这个映射下寻找一个特殊的子集 S，这个子集满足某种条件：通过递归和移除元素，最终形成一个满足特定映射关系的子集。
> 背景
> 假设 f 是集合 A 上的一种映射，我们关心的是在此映射下，如何得到一个满足特定性质的子集 S，并且这个子集尽量保持“稳定”或“最大”。这类问题通常出现在一些优化问题中，尤其是和不动点理论、图论中的强连通分量、数据库中的依赖关系以及某些形式的闭包操作相关。
> 关键问题分析
> 在你描述的算法中，核心的操作是：
>
> 1.检查是否存在某个元素 k，它没有其他元素映射到它上：
> 这说明我们正在寻找某些特殊的元素，可能是“孤立”的元素或“固定点”元素，即这些元素的映射不受其他元素的影响。
> 2.移除这样一个元素，并递归调用算法：
> 如果找到了这样一个元素，就将其移除，意味着我们正在逐步减少集合中的元素，并通过递归来简化问题。
> 3.无法找到这样的元素时返回当前集合：
> 当无法继续移除元素时，算法返回当前的集合，意味着此时的集合 A 已经无法进一步简化。
>
> 为什么要找有元素映射到其上的最大子集？
> 在这种背景下，算法的目标通常是找到集合中的一个子集 S，使得：
>
> 4.子集 S 中的元素在映射下具有某种特性（比如被映射到自己或者其他元素不再映射到它）。
> 5.该子集满足某种稳定性或最大性条件，比如不再包含可以移除的元素。
>
> 这与一些依赖关系分析、图论中的强连通分量或者闭包操作有密切关系。通过递归和移除元素，我们在构建一个符合条件的子集 S，这个子集在映射关系上可能是一个不动点或封闭的结构。例如，考虑一个依赖图，其中每个节点代表某个元素，每条边代表元素之间的映射或依赖关系。我们可能希望找到一个集合，该集合中的每个元素都与其他元素有某种形式的依赖或映射关系，从而不能再从中移除任何元素。
> 相关应用场景
> 这种类型的算法通常用于处理以下问题：
>
> 6.闭包运算：例如，传递闭包、依赖闭包等。在这些问题中，我们需要找到一个在映射下不可再简化的集合，类似于求解“最大子集”。
> 7.图论问题：像强连通分量的检测或图的遍历中，寻找与映射关系相关的最大子图（例如，满足某些映射不变性的部分子图）。
> 8.递归依赖关系：比如数据库中的依赖分析，寻找稳定的或最大依赖关系集。
>
> 总结
> 这个算法的背景涉及在给定映射下，通过逐步移除某些元素来找到一个“最大”子集，使得该子集中的元素具有稳定性（或映射关系上的某种不动点特性）。在实际应用中，这种方法通常与依赖关系分析、图论中的强连通分量、递归闭包等相关，目的是找到一个不可进一步简化的子集或结构。

- PA3: 

  - 最大子集问题：

    ```python
    """
    伪代码提示
    Mapping(A, f)算法
    输入：
    集合A；
    集合A到集合A的映射f；
    输出：
    满足条件的子集S；
    """
     if 集合A只有1个元素 then
        return A
     else if 能找到一个没有其他元素映射到其上的元素，设为k then
        A = A – {k}；
        f =从f中删除所有包含k的映射关系；
        return Mapping(A, f)；
     else
        return A；
     end if
    ```

    