#include "AdjacencyMatrix.h"
#include <iostream>

AdjacencyMatrix::AdjacencyMatrix(int vertices, bool directed, bool weighted)
    : BaseGraph(vertices, directed, weighted)
{
    // 初始化邻接矩阵，所有元素置为0
    matrix.resize(vertices, std::vector<int>(vertices, 0));
}

void AdjacencyMatrix::addEdge(int s, int d, int w)
{
    // 首先调用基类的addEdge来维护边的列表
    BaseGraph::addEdge(s, d, w);

    // 在邻接矩阵中添加边
    matrix[s][d] = w;

    // 如果是无向图，则需要添加反向边
    if (!isDirected)
    {
        matrix[d][s] = w;
    }
}

int AdjacencyMatrix::getWeight(int s, int d) const
{
    return matrix[s][d];
}

const std::vector<std::vector<int>> &AdjacencyMatrix::getMatrix() const
{
    return matrix;
}

void AdjacencyMatrix::printMatrix() const
{
    for (int i = 0; i < numVertices; ++i)
    {
        for (int j = 0; j < numVertices; ++j)
        {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int AdjacencyMatrix::getEdgeCount() const
{
    int count = 0;
    for (int i = 0; i < numVertices; ++i)
    {
        for (int j = 0; j < numVertices; ++j)
        {
            if (matrix[i][j] != 0)
            {
                count++;
            }
        }
    }
}