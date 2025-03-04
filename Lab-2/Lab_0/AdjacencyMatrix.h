// 继承自图的base类
#ifndef __ADJACENCYMATRIX_H__
#define __ADJACENCYMATRIX_H__

#include "BaseGraph.h"
#include <vector>

class AdjacencyMatrix : public BaseGraph
{
private:
    std::vector<std::vector<int>> matrix;

public:
    // 构造函数
    AdjacencyMatrix(int vertices, bool directed = false, bool weighted = false);

    // 添加边
    void addEdge(int s, int d, int w = 1);

    // 获取两点间的边权值，如果边不存在返回0
    int getWeight(int s, int d) const;

    // 获取邻接矩阵
    const std::vector<std::vector<int>> &getMatrix() const;

    // 打印邻接矩阵
    void printMatrix() const;

    // 获取边的数量
    int getEdgeCount() const;

    // 获取节点的直接前驱
    std::vector<int> getPredecessors(int v) const;

    // 获取节点的直接后继
    std::vector<int> getSuccessors(int v) const;
};

#endif // __ADJACENCYMATRIX_H__