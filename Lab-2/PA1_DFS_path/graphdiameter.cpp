#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

class Graph {
private:
    int n; 
    int m; 
    std::vector<std::vector<int>> dist; 
    const int INF = std::numeric_limits<int>::max() / 2; 

public:
    Graph(int vertices, int edges) : n(vertices), m(edges) {
        dist.resize(n + 1, std::vector<int>(n + 1, INF));
        for (int i = 1; i <= n; ++i) {
            dist[i][i] = 0;
        }
    }

    void addEdge(int u, int v, int w) {
        dist[u][v] = std::min(dist[u][v], w);
        dist[v][u] = std::min(dist[v][u], w); 
    }

    void floydWarshall() {
        for (int k = 1; k <= n; ++k) {
            for (int i = 1; i <= n; ++i) {
                if (dist[i][k] == INF) continue;  // 新增剪枝优化
                for (int j = 1; j <= n; ++j) {
                    dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }

    int getDiameter() {
        floydWarshall();
        int diameter = 0;
        for (int i = 1; i <= n; ++i) {
            // 合并连通性检查和直径计算
            int max_dist = *std::max_element(dist[i].begin() + 1, dist[i].begin() + n + 1);
            if (max_dist == INF) return -1;
            diameter = std::max(diameter, max_dist);
        }
        return diameter;
    }
};
int main()
{
    int n, m;
    std::cin >> n >> m;
    Graph graph(n, m);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        std::cin >> u >> v >> w;
        graph.addEdge(u, v, w);
    }
    int diameter = graph.getDiameter();
    std::cout << diameter << std::endl;
    return 0;
}