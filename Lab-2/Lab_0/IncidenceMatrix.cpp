#include "IncidenceMatrix.h"
#include <iostream>

IncidenceMatrix::IncidenceMatrix(int vertices, bool directed, bool weighted)
    : BaseGraph(vertices, directed, weighted), edgeCount(0)
{
    // 初始化关联矩阵为空
    matrix.resize(vertices);
}

void IncidenceMatrix::addEdge(int s, int d, int w)
{
    // 首先调用基类的addEdge来维护边的列表
    BaseGraph::addEdge(s, d, w);

    // 调整矩阵大小以容纳新边
    for (int i = 0; i < numVertices; ++i)
    {
        matrix[i].resize(edgeCount + 1, 0);
    }

    if (isDirected)
    {
        // 有向图：起点设为-1，终点设为1（如果带权重则使用实际权重）
        matrix[s][edgeCount] = isWeighted ? -w : -1;
        matrix[d][edgeCount] = isWeighted ? w : 1;
    }
    else
    {
        // 无向图：相连顶点设为1（如果带权重则使用实际权重）
        matrix[s][edgeCount] = isWeighted ? w : 1;
        matrix[d][edgeCount] = isWeighted ? w : 1;
    }

    ++edgeCount;
}

const std::vector<std::vector<int>> &IncidenceMatrix::getMatrix() const
{
    return matrix;
}

int IncidenceMatrix::getEdgeCount() const
{
    return edgeCount;
}

void IncidenceMatrix::printMatrix() const
{
    std::cout << "关联矩阵 (" << numVertices << " 顶点, " << edgeCount << " 边):\n";
    for (int i = 0; i < numVertices; ++i)
    {
        for (int j = 0; j < edgeCount; ++j)
        {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}