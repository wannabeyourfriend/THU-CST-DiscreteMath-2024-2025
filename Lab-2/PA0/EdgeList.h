#ifndef __EDGELIST_H__
#define __EDGELIST_H__

#include "BaseGraph.h"
#include <vector>

class EdgeList : public BaseGraph
{
private:
    std::vector<int> startVertices; // 存储边的起始顶点
    std::vector<int> endVertices;   // 存储边的终止顶点
    std::vector<int> weights;       // 存储边的权重

public:
    // 构造函数
    EdgeList(int vertices, bool directed = false, bool weighted = false);

    // 添加边
    void addEdge(int s, int d, int w = 1);

    // 获取边列表信息
    const std::vector<int> &getStartVertices() const;
    const std::vector<int> &getEndVertices() const;
    const std::vector<int> &getWeights() const;

    // 打印边列表
    void printList() const;
};

#endif // __EDGELIST_H__