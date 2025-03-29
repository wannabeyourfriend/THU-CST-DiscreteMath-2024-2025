#include "WeightMatrix.h"
#include <iostream>

WeightMatrix::WeightMatrix(int vertices, bool directed, bool weighted)
    : BaseGraph(vertices, directed, true)
{ // 注意：权重矩阵总是带权重的
    // 初始化权重矩阵，所有元素置为INF，对角线置为0
    matrix.resize(vertices, std::vector<int>(vertices, INF));
    for (int i = 0; i < vertices; ++i)
    {
        matrix[i][i] = 0;
    }
}

void WeightMatrix::addEdge(int s, int d, int w)
{
    // 首先调用基类的addEdge来维护边的列表
    BaseGraph::addEdge(s, d, w);

    // 在权重矩阵中添加边
    matrix[s][d] = w;

    // 如果是无向图，则需要添加反向边
    if (!isDirected)
    {
        matrix[d][s] = w;
    }
}

int WeightMatrix::getWeight(int s, int d) const
{
    return matrix[s][d];
}

const std::vector<std::vector<int>> &WeightMatrix::getMatrix() const
{
    return matrix;
}

void WeightMatrix::printMatrix() const
{
    for (int i = 0; i < numVertices; ++i)
    {
        for (int j = 0; j < numVertices; ++j)
        {
            if (matrix[i][j] == INF)
            {
                std::cout << "INF ";
            }
            else
            {
                std::cout << matrix[i][j] << " ";
            }
        }
        std::cout << std::endl;
    }
}

std::vector<int> WeightMatrix::getPredecessors(int node) const
{
    std::vector<int> predecessors;
    for (int i = 0; i < numVertices; ++i)
    {
        if (matrix[i][node] != INF)
        {
            predecessors.push_back(i);
        }
    }
    return predecessors;
}

std::vector<int> WeightMatrix::getSuccessors(int node) const
{
    std::vector<int> successors;
    for (int i = 0; i < numVertices; ++i)
    {
        if (matrix[node][i] != INF)
        {
            successors.push_back(i);
        }
    }
    return successors;
}