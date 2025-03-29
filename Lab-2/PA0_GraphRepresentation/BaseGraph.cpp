// BaseGraph.cpp
#include "BaseGraph.h"

BaseGraph::BaseGraph(int vertices, bool directed, bool weighted)
    : numVertices(vertices), isDirected(directed), isWeighted(weighted) {}

void BaseGraph::addEdge(int s, int d, int w)
{
    edges.emplace_back(s, d, w);
    if (!isDirected)
    {
        edges.emplace_back(d, s, w);
    }
}

int BaseGraph::getNumVertices() const { return numVertices; }
bool BaseGraph::isDirectedGraph() const { return isDirected; }
bool BaseGraph::isWeightedGraph() const { return isWeighted; }
const std::vector<Edge> &BaseGraph::getEdges() const { return edges; }