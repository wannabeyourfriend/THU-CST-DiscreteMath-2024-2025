#ifndef __WEIGHTMATRIX_H__
#define __WEIGHTMATRIX_H__

#include "BaseGraph.h"
#include <vector>
#include <limits>

class WeightMatrix : public BaseGraph
{
private:
    std::vector<std::vector<int>> matrix;
    const int INF = std::numeric_limits<int>::max();

public:
    // 构造函数
    WeightMatrix(int vertices, bool directed = false, bool weighted = true);

    // 添加边
    void addEdge(int s, int d, int w = 1);

    // 获取两点间的权值，如果边不存在返回INF
    int getWeight(int s, int d) const;

    // 获取权重矩阵
    const std::vector<std::vector<int>> &getMatrix() const;

    // 打印权重矩阵
    void printMatrix() const;

    // 返回节点的直接前驱
    std::vector<int> getPredecessors(int node) const;

    // 返回节点的直接后继
    std::vector<int> getSuccessors(int node) const;
};

#endif // __WEIGHTMATRIX_H__