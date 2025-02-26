## 离散（2）hw1

> 王子轩 `2023011307`
>
> `wang-zx23@mails.tsinghua.edu.cn`

### P14 T16

> 写出如图的邻接矩阵、关联矩阵、边列表、正向表

![image-20250226202149012](C:\Users\35551\AppData\Roaming\Typora\typora-user-images\image-20250226202149012.png)

```python
import networkx as nx
import matplotlib.pyplot as plt
DG = nx.DiGraph()
DG.add_node("v1")
DG.add_node("v2")
DG.add_node("v3")
DG.add_node("v4")
DG.add_node("v5")
DG.add_node("v6")
DG.add_edge("v1", "v2")
DG.add_edge("v1", "v4")
DG.add_edge("v2", "v5")
DG.add_edge("v3", "v1")
DG.add_edge("v3", "v4")
DG.add_edge("v5", "v3")
DG.add_edge("v6", "v1")
DG.add_edge("v6", "v3")
DG.add_edge("v6", "v4")
nx.draw(DG, with_labels=True, font_weight='bold', node_size=500, node_color='lightblue', font_size=15, arrowsize=20)
```

```
{'v1': ['v2', 'v4'], 
'v2': ['v5'], 
'v3': ['v1', 'v4'], 
'v4': [], 
'v5': ['v3'], 
'v6': ['v1', 'v3', 'v4']}
```

- 邻接矩阵
  $$
  \mathbf{A} =\begin{bmatrix}
  0 & 1 & 0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 0 & 1 & 0 \\
  1 & 0 & 0 & 1 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 & 0 \\
  1 & 0 & 1 & 1 & 0 & 0
  \end{bmatrix}
  $$

- 关联矩阵
  $$
  \mathbf{B} = \begin{bmatrix}
  1 & 1 & 0 & -1& 0 & 0 & -1& 0 & 0 \\
  -1& 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
  0 & 0 & 0 & 1 & 1 & -1& 0 & -1 & 0 \\
  0 & -1& 0 & 0 & -1& 0 & 0 & 0 & -1 \\
  0 & 0 & -1& 0 & 0 & 1 & 0 & 0 & 0 \\
  0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 \\  
  \end{bmatrix}
  $$

- 边列表
  $$
  \mathbf{A} = \begin{bmatrix} 1 & 1 & 2 & 3 & 3 & 5 & 6 & 6 & 6 \end{bmatrix}\\
  \mathbf{B} = \begin{bmatrix}2 & 4 & 5 & 1 & 4 & 3 & 1 & 3 & 4 \end{bmatrix}
  $$

- 正向表
  $$
  \begin{aligned}
  & \mathbf{A} = \begin{bmatrix} 1 & 3 & 4 & 6 & 6 & 7  \end{bmatrix}\\
   &\mathbf{B} = \begin{bmatrix}2 & 4 & 5 & 1 & 4 & 3 & 1 & 3 & 4 \end{bmatrix}
  \end{aligned}
  $$

### P14 T17

>

### P14 T21