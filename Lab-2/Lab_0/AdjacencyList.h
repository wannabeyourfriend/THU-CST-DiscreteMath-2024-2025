#ifndef __ADJACENCYLIST_H__
#define __ADJACENCYLIST_H__

#include "BaseGraph.h"
#include <vector>

// 邻接表节点结构
struct ListNode
{
    int dst;        // 邻接点编号
    int weight;     // 边权值
    ListNode *next; // 指向下一个节点的指针

    ListNode(int d, int w = 1, ListNode *n = nullptr)
        : dst(d), weight(w), next(n) {}
};

class AdjacencyList : public BaseGraph
{
private:
    std::vector<ListNode *> adjList; // 邻接表数组

    // 清理邻接表内存
    void clearList();

public:
    // 构造函数和析构函数
    AdjacencyList(int vertices, bool directed = false, bool weighted = false);
    ~AdjacencyList();

    // 添加边
    void addEdge(int s, int d, int w = 1);

    // 获取指定顶点的邻接表头节点
    ListNode *getAdjList(int vertex) const;

    // 打印邻接表
    void printList() const;
};

#endif // __ADJACENCYLIST_H__