#include "ForwardReverseTable.h"
#include <iostream>
#include <map>

ForwardReverseTable::ForwardReverseTable(int vertices, bool directed, bool weighted)
    : BaseGraph(vertices, directed, weighted)
{
    // 初始化A数组大小为顶点数+1
    forwardA.resize(vertices + 1);
    reverseA.resize(vertices + 1);
}

void ForwardReverseTable::addEdge(int s, int d, int w)
{
    BaseGraph::addEdge(s, d, w);
    buildTables(); // 每次添加边后重建表
}

void ForwardReverseTable::buildTables()
{
    // 清空现有的B数组和权重数组
    forwardB.clear();
    reverseB.clear();
    weights.clear();

    // 创建临时映射来存储每个起始顶点的边
    std::map<int, std::vector<std::pair<int, int>>> forwardMap;
    std::map<int, std::vector<std::pair<int, int>>> reverseMap;

    // 处理所有边
    for (const Edge &edge : edges)
    {
        forwardMap[edge.source].push_back({edge.destination, edge.weight});
        if (!isDirected)
        {
            forwardMap[edge.destination].push_back({edge.source, edge.weight});
        }
        reverseMap[edge.destination].push_back({edge.source, edge.weight});
        if (!isDirected)
        {
            reverseMap[edge.source].push_back({edge.destination, edge.weight});
        }
    }

    // 构建正向表
    int currentIndex = 0;
    for (int i = 0; i < numVertices; ++i)
    {
        forwardA[i] = currentIndex;
        auto it = forwardMap.find(i);
        if (it != forwardMap.end())
        {
            // 对直接后继节点排序
            std::sort(it->second.begin(), it->second.end());
            for (const auto &pair : it->second)
            {
                forwardB.push_back(pair.first);
                weights.push_back(pair.second);
                ++currentIndex;
            }
        }
    }
    forwardA[numVertices] = currentIndex; // 设置A[n] = m + 1

    // 构建逆向表
    currentIndex = 0;
    for (int i = 0; i < numVertices; ++i)
    {
        reverseA[i] = currentIndex;
        auto it = reverseMap.find(i);
        if (it != reverseMap.end())
        {
            // 对直接前驱节点排序
            std::sort(it->second.begin(), it->second.end());
            for (const auto &pair : it->second)
            {
                reverseB.push_back(pair.first);
                ++currentIndex;
            }
        }
    }
    reverseA[numVertices] = currentIndex;
}

const std::vector<int> &ForwardReverseTable::getForwardA() const
{
    return forwardA;
}

const std::vector<int> &ForwardReverseTable::getForwardB() const
{
    return forwardB;
}

const std::vector<int> &ForwardReverseTable::getReverseA() const
{
    return reverseA;
}

const std::vector<int> &ForwardReverseTable::getReverseB() const
{
    return reverseB;
}

const std::vector<int> &ForwardReverseTable::getWeights() const
{
    return weights;
}

void ForwardReverseTable::printTables() const
{
    std::cout << "正向表：" << std::endl;
    std::cout << "A数组: ";
    for (int x : forwardA)
        std::cout << x << " ";
    std::cout << "\nB数组: ";
    for (int x : forwardB)
        std::cout << x << " ";

    if (isWeighted)
    {
        std::cout << "\n权重: ";
        for (int w : weights)
            std::cout << w << " ";
    }

    std::cout << "\n\n逆向表：" << std::endl;
    std::cout << "A数组: ";
    for (int x : reverseA)
        std::cout << x << " ";
    std::cout << "\nB数组: ";
    for (int x : reverseB)
        std::cout << x << " ";
    std::cout << std::endl;
}