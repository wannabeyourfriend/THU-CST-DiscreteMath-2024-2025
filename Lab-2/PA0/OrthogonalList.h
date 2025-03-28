#ifndef __ORTHOGONALLIST_H__
#define __ORTHOGONALLIST_H__

#include "BaseGraph.h"
#include <vector>

// 边节点结构
struct EdgeNode
{
    int src;          // 边的起点
    int dst;          // 边的终点
    int weight;       // 边的权重
    EdgeNode *d_link; // 指向下一个相同终点的边
    EdgeNode *s_link; // 指向下一个相同起点的边

    EdgeNode(int s, int d, int w = 1)
        : src(s), dst(d), weight(w), d_link(nullptr), s_link(nullptr) {}
};

// 顶点节点结构
struct VertexNode
{
    int data;      // 顶点数据
    EdgeNode *in;  // 指向第一条以该顶点为终点的边
    EdgeNode *out; // 指向第一条以该顶点为起点的边

    VertexNode(int d = 0) : data(d), in(nullptr), out(nullptr) {}
};

class OrthogonalList : public BaseGraph
{
private:
    std::vector<VertexNode> vertices; // 顶点数组

    // 清理边节点内存
    void clearEdges();

public:
    // 构造函数和析构函数
    OrthogonalList(int vertices, bool directed = true, bool weighted = false);
    ~OrthogonalList();

    // 添加边
    void addEdge(int s, int d, int w = 1);

    // 获取顶点的入边和出边
    EdgeNode *getFirstIn(int vertex) const;
    EdgeNode *getFirstOut(int vertex) const;

    // 打印十字链表
    void printList() const;
};

#endif // __ORTHOGONALLIST_H__