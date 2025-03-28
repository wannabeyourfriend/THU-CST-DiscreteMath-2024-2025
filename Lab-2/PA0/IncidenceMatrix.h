#ifndef __INCIDENCEMATRIX_H__
#define __INCIDENCEMATRIX_H__

#include "BaseGraph.h"
#include <vector>

class IncidenceMatrix : public BaseGraph
{
private:
    std::vector<std::vector<int>> matrix;
    int edgeCount; // 记录边的数量

public:
    // 构造函数
    IncidenceMatrix(int vertices, bool directed = false, bool weighted = false);

    // 添加边
    void addEdge(int s, int d, int w = 1);

    // 获取关联矩阵
    const std::vector<std::vector<int>> &getMatrix() const;

    // 获取边的数量
    int getEdgeCount() const;

    // 打印关联矩阵
    void printMatrix() const;
};

#endif // __INCIDENCEMATRIX_H__