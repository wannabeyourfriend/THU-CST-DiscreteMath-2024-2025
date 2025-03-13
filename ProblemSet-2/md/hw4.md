## 离散（2）hw4

> 王子轩 `2023011307`
>
> `wang-zx23@mails.tsinghua.edu.cn`

### P50 T11

> 是否存在如P51图2.42的一条路经过各门一次？试说明理由。

解：我们可以将原图建模为下图

![3c2b62b1e2d53f87d22194fe3df6fb2](C:\Users\35551\Documents\WeChat Files\wxid_vk41xij7zufd22\FileStorage\Temp\3c2b62b1e2d53f87d22194fe3df6fb2.jpg)

存在道路$P = (C-A-B-F-C-D-B-E-F-D-E)$.

理由：$G(V,E)$中度数为奇点的vertex数量为2，由书上的推论P28 2.3.1可知存在欧拉道路。

### P51 T12

>判断图2.43中的图形，至少需要几笔才能画出，并写出具体方案。

解：

(a)：由图中有4个度数为奇数的顶点，因此至少需要2笔。   $P_1 = v_5v_4v_2v_0v_4v_1v_5v_0 \quad P_2 = v_3v_2$

(b)：由图中有4个度数为奇数的顶点，因此至少需要2笔。$P_1 = v_1v_0v_4 \quad P_2 = v_5v_6v_7v_0v_2v_7v_3v_2$

(c)：至少需要两笔。$P_1 = v_1v_2v_0v_5 \quad P_2 = v_1v_0v_4v_3$

(d)：至少需要一笔，只包含两个度数为奇数的顶点，存在欧拉道路。$P = v_3v_6v_2v_3v_5v_6v_4v_1v_2v_4v_5v_1v_6$