#ifndef __BASEGRAPH_H__
#define __BASEGRAPH_H__
#include <vector>

struct Edge
{
    int source;
    int destination;
    int weight;
    Edge(int s, int d, int w = 1) : source(s), destination(d), weight(w) {}
};

class BaseGraph
{
protected:
    int numVertices;
    bool isDirected;
    bool isWeighted;
    std::vector<Edge> edges;

public:
    BaseGraph(int vertices, bool directed = false, bool weighted = false);
    void addEdge(int s, int d, int w = 1);
    int getNumVertices() const;
    bool isDirectedGraph() const;
    bool isWeightedGraph() const;
    const std::vector<Edge> &getEdges() const;
};

#endif // __BASEGRAPH_H__