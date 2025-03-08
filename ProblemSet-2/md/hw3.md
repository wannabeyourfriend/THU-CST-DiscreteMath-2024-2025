## 离散（2）hw3

> 王子轩 `2023011307`
>
> `wang-zx23@mails.tsinghua.edu.cn`

### P50 T1

> 设简单图$G(m,n)$有$k$个连通支，证明$m \leq \frac{1}{2}(n - k + 1)(n - k)$

解：不妨设这k个连通支分别为$G_1, \cdots G_k$,阶数分别是$n_1, \cdots n_k$边数分别为$m_1, \cdots m_k$.由于$\forall i , n_i \geq 1 \text{ and } \sum_i n_i = n $所以$n_i \leq n - k +1$；由于连通支内部边数最多是正则图，即$m_i \leq \frac{1}{2}(n_i - 1)n_i$.因此有$m = \sum m_i \leq \sum_i [\frac{1}{2}(n_i - 1)n_i] \leq \frac{1}{2}(n_i-1)(n -k +1) \leq \frac{1}{2}(\sum n_i -k)(n - k + 1) = \frac{1}{2}(n - k + 1)(n - k)$

### P50 T2

> 证明G和G的补图中至少有一个是连通图

证明：假设$G(V, E)$是不连通的，下证其补图$\overline{G}(V',E')$一定是连通的:设$V_1, V_2, \cdots, V_k$是它的的$k$个连通支的点集，即$V = V_1 \cup \cdots V_k$.任意的$u,v \in V$

- $\text{ if }u \in V_i, v \in V_j, i \neq j, (u,v) \in E'$ thus $\exist P(u, v)$
- $\text{ if }u, v \in V_i, \forall s \in V_j, j \neq i, (u, s) \in E',(s, v) \in E'$ thus $\exists P(u,s,v)$

综上，若$G$不是连通图，$\overline{G}$一定是连通的。

### P50 T3

> 证明若连通图的最长路径不唯一，则必定相交

证明: 我们采用反证法，不妨设$G(V,E)$两条相同长度的最长路分别为$l_1$和$l_2$,其长度为$k$；由于G是连通图，一定有：$\exists u \in l_1 \text{  and } v \in l_2 \text{ and } (u,v) \in E$ .$u, v$分别可以作为$l_1$和$l_2$的分割点，我们分别找出其中较长的那一段,分别记录为$l_1'$和$l_2'$,显然有$l_1', l_2' \geq \lceil \frac{k}{2} \rceil$那么我们找到新的路径$P'= l_1'-(u,v)-l_2'$长度为$\lceil \frac{k}{2} \rceil \times 2 + 1 \geq k$

### P50 T4

> 在简单图$G(n,m)$中，如果$n \geq 4$并且$m \geq 2n-3$,证明$G$中含有带弦的回路

证明：**Lemma**: 如果一个简单图$G$它的极长初级道路的端点度数$\geq 3$,则$G$一定存在带弦的回路. 

引理证明如下：记极长初级道路为$P(v_1v_2\cdots v_j)$,其中$d(v_j) \geq 3$,则$v_j$一定会连到其他的$v_a, v_b, \quad a, b \in [1, j)$上，由于$P$是极长的道路,$v_a, v_b$必处在$P$上，不妨设$a < b$,那么$(v_b\cdots v_j v_b)$组成了回路$C$,而$e = (v_j, v_a)$为其上的弦.

接下来我们使用数学归纳法来证明原命题：

- 归纳奠基：对于$n = 4， m \geq 5$时候，$G$中必然存在带弦的回路
- 归纳假设：假设对于$n = k, m \geq 2k - 3$, 则$G$中含有带弦的回路
- 归纳地推：对于$n = k + 1, m \geq 2(k + 1)- 3 = 2k -1$情形，对于$G$中的极长初级道路$P$, 其端点$v$的$d(v) $若$\geq 3$则由Lemma保证$G$一定存在带弦的回路. 若$d(v) \leq 2$那么$G$的子图$G - \{v\}$满足$n = k，m \geq 2k -3$，由归纳假设知道$G - \{v\}$中一定存在带弦的回路，则$G$中存在带弦的回路。

### P50 T5

> 设$G$是不存在$K_3$回路的简单图，证明
>
> (1) $\sum_i d^2(v_i) \leq mn$
>
> (2) $m \leq \frac{n^2}{4}$

证明：

(1) 设$G$的阶数为$n$,考虑图中的节点$(u, v)$之间有边，由于$G$中不存在$K_3$因此显然有$d(u) -1 + d(v) - 1 \leq n - 2$即有$d(u) + d(v) \leq n$对左右分别对所有的边$e =(u, v) \in E$求和，即$\sum_{e \in E}[d(u) + d(v)] \leq mn , \quad u  \neq v$,左边是对全体的边求和，而一条边会对节点$v$贡献$d(v)$，因此上式子化为$\sum_i d^2(v_i) \leq mn$.

(2) 利用$Jensen$不等式，对于下凸函数$f(X) = \sum_i X^2_i$有$Ef(X) \geq f(EX)$因此有$\frac{\sum_i d^2(v_i)}{n} \geq (\frac{d(v_i)}{n})^2 = (\frac{2m}{n})^2$. 再利用第一问的结论$\sum_i d^2(v_i) \leq mn$我们有$m \geq 4m^2/n^2$ 整理得到$m \leq \frac{n^2}{4}$
