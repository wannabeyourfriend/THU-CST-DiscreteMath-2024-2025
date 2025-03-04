#include "OrthogonalList.h"
#include <iostream>

OrthogonalList::OrthogonalList(int vertexCount, bool directed, bool weighted)
    : BaseGraph(vertexCount, directed, weighted)
{
    // 初始化顶点数组
    vertices.resize(vertexCount);
    for (int i = 0; i < vertexCount; ++i)
    {
        vertices[i].data = i;
    }
}

OrthogonalList::~OrthogonalList()
{
    clearEdges();
}

void OrthogonalList::clearEdges()
{
    // 遍历所有顶点的出边链表，释放边节点内存
    for (int i = 0; i < numVertices; ++i)
    {
        EdgeNode *current = vertices[i].out;
        while (current != nullptr)
        {
            EdgeNode *next = current->s_link;
            delete current;
            current = next;
        }
    }
}

void OrthogonalList::addEdge(int s, int d, int w)
{
    BaseGraph::addEdge(s, d, w);

    // 创建新的边节点
    EdgeNode *newEdge = new EdgeNode(s, d, w);

    // 处理出边链表（按目标顶点编号排序）
    if (vertices[s].out == nullptr || vertices[s].out->dst >= d)
    {
        newEdge->s_link = vertices[s].out;
        vertices[s].out = newEdge;
    }
    else
    {
        EdgeNode *current = vertices[s].out;
        while (current->s_link != nullptr && current->s_link->dst < d)
        {
            current = current->s_link;
        }
        newEdge->s_link = current->s_link;
        current->s_link = newEdge;
    }

    // 处理入边链表（按源顶点编号排序）
    if (vertices[d].in == nullptr || vertices[d].in->src >= s)
    {
        newEdge->d_link = vertices[d].in;
        vertices[d].in = newEdge;
    }
    else
    {
        EdgeNode *current = vertices[d].in;
        while (current->d_link != nullptr && current->d_link->src < s)
        {
            current = current->d_link;
        }
        newEdge->d_link = current->d_link;
        current->d_link = newEdge;
    }

    // 如果是无向图，添加反向边并建立相应的链接
    if (!isDirected)
    {
        EdgeNode *reverseEdge = new EdgeNode(d, s, w);

        // 处理反向边的出边链表
        if (vertices[d].out == nullptr || vertices[d].out->dst >= s)
        {
            reverseEdge->s_link = vertices[d].out;
            vertices[d].out = reverseEdge;
        }
        else
        {
            EdgeNode *current = vertices[d].out;
            while (current->s_link != nullptr && current->s_link->dst < s)
            {
                current = current->s_link;
            }
            reverseEdge->s_link = current->s_link;
            current->s_link = reverseEdge;
        }

        // 处理反向边的入边链表
        if (vertices[s].in == nullptr || vertices[s].in->src >= d)
        {
            reverseEdge->d_link = vertices[s].in;
            vertices[s].in = reverseEdge;
        }
        else
        {
            EdgeNode *current = vertices[s].in;
            while (current->d_link != nullptr && current->d_link->src < d)
            {
                current = current->d_link;
            }
            reverseEdge->d_link = current->d_link;
            current->d_link = reverseEdge;
        }
    }
}
EdgeNode *OrthogonalList::getFirstIn(int vertex) const
{
    if (vertex >= 0 && vertex < numVertices)
    {
        return vertices[vertex].in;
    }
    return nullptr;
}

EdgeNode *OrthogonalList::getFirstOut(int vertex) const
{
    if (vertex >= 0 && vertex < numVertices)
    {
        return vertices[vertex].out;
    }
    return nullptr;
}

void OrthogonalList::printList() const
{
    std::cout << "十字链表表示：" << std::endl;

    for (int i = 0; i < numVertices; ++i)
    {
        std::cout << "顶点 " << i << ":\n";

        // 打印出边
        std::cout << "  出边: ";
        EdgeNode *out = vertices[i].out;
        while (out != nullptr)
        {
            std::cout << i << "->" << out->dst;
            if (isWeighted)
            {
                std::cout << "(权重:" << out->weight << ")";
            }
            std::cout << " ";
            out = out->s_link;
        }
        std::cout << "\n";

        // 打印入边
        std::cout << "  入边: ";
        EdgeNode *in = vertices[i].in;
        while (in != nullptr)
        {
            std::cout << in->src << "->" << i;
            if (isWeighted)
            {
                std::cout << "(权重:" << in->weight << ")";
            }
            std::cout << " ";
            in = in->d_link;
        }
        std::cout << "\n";
    }
}