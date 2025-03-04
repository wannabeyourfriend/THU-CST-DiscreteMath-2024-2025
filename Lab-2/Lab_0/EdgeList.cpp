#include "EdgeList.h"
#include <iostream>

EdgeList::EdgeList(int vertices, bool directed, bool weighted)
    : BaseGraph(vertices, directed, weighted)
{
}

void EdgeList::addEdge(int s, int d, int w)
{
    // 首先调用基类的addEdge来维护边的列表
    BaseGraph::addEdge(s, d, w);

    // 添加到边列表
    startVertices.push_back(s);
    endVertices.push_back(d);
    weights.push_back(w);

    // 如果是无向图，则添加反向边
    if (!isDirected)
    {
        startVertices.push_back(d);
        endVertices.push_back(s);
        weights.push_back(w);
    }
}

const std::vector<int> &EdgeList::getStartVertices() const
{
    return startVertices;
}

const std::vector<int> &EdgeList::getEndVertices() const
{
    return endVertices;
}

const std::vector<int> &EdgeList::getWeights() const
{
    return weights;
}

void EdgeList::printList() const
{
    std::cout << "边列表表示：" << std::endl;
    std::cout << "图类型: " << (isDirected ? "有向" : "无向")
              << (isWeighted ? "带权" : "无权") << "图" << std::endl;

    for (size_t i = 0; i < startVertices.size(); ++i)
    {
        std::cout << "边 " << i << ": "
                  << startVertices[i] << " -> "
                  << endVertices[i];
        if (isWeighted)
        {
            std::cout << " (权重: " << weights[i] << ")";
        }
        std::cout << std::endl;
    }
}