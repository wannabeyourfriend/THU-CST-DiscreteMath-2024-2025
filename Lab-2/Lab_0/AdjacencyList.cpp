#include "AdjacencyList.h"
#include <iostream>

AdjacencyList::AdjacencyList(int vertices, bool directed, bool weighted)
    : BaseGraph(vertices, directed, weighted)
{
    // 初始化邻接表数组
    adjList.resize(vertices, nullptr);
}

AdjacencyList::~AdjacencyList()
{
    clearList();
}

void AdjacencyList::clearList()
{
    // 释放所有链表节点的内存
    for (int i = 0; i < numVertices; ++i)
    {
        ListNode *current = adjList[i];
        while (current != nullptr)
        {
            ListNode *next = current->next;
            delete current;
            current = next;
        }
        adjList[i] = nullptr;
    }
}

void AdjacencyList::addEdge(int s, int d, int w)
{
    // 调用基类的addEdge来维护边的列表
    BaseGraph::addEdge(s, d, w);

    // 在邻接表中添加边
    ListNode *newNode = new ListNode(d, w);
    newNode->next = adjList[s];
    adjList[s] = newNode;

    // 如果是无向图，则需要添加反向边
    if (!isDirected)
    {
        newNode = new ListNode(s, w);
        newNode->next = adjList[d];
        adjList[d] = newNode;
    }
}

ListNode *AdjacencyList::getAdjList(int vertex) const
{
    if (vertex >= 0 && vertex < numVertices)
    {
        return adjList[vertex];
    }
    return nullptr;
}

void AdjacencyList::printList() const
{
    std::cout << "邻接表表示：" << std::endl;
    for (int i = 0; i < numVertices; ++i)
    {
        std::cout << i << " -> ";
        ListNode *current = adjList[i];
        while (current != nullptr)
        {
            std::cout << current->dst;
            if (isWeighted)
            {
                std::cout << "(权重:" << current->weight << ")";
            }
            if (current->next != nullptr)
            {
                std::cout << " -> ";
            }
            current = current->next;
        }
        std::cout << std::endl;
    }
}