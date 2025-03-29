#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_set>

class Graph {
private:
    int vertices;
    int edges;
    std::vector<int> A;  
    std::vector<int> B;  
    std::vector<bool> visited;
    std::vector<std::vector<int>> allPaths;
    std::vector<int> currentPath;
    std::vector<std::vector<int>> adjacencyList; 

    void dfs(int current, int target) {
        visited[current] = true;
        currentPath.push_back(current);

        if (current == target) {
            allPaths.push_back(currentPath);
        } else {
            for (int next : adjacencyList[current]) {
                if (!visited[next]) {
                    dfs(next, target);
                }
            }
        }

        visited[current] = false;
        currentPath.pop_back();
    }

public:
    Graph(int v, int e) : vertices(v), edges(e) {
        A.resize(v + 1);
        visited.resize(v, false);
        adjacencyList.resize(v); // 初始化邻接表
    }

    void readGraph() {
        for (int i = 0; i <= vertices; i++) {
            std::cin >> A[i];
        }

        B.resize(edges);
        for (int i = 0; i < edges; i++) {
            std::cin >> B[i];
        }

        // 构建去重的邻接表
        for (int i = 0; i < vertices; i++) {
            int start = A[i];
            int end = A[i + 1];
            std::vector<int> neighbors;
            
            // 收集所有邻接点
            for (int j = start; j < end; j++) {
                neighbors.push_back(B[j]);
            }
            
            // 排序并去重
            std::sort(neighbors.begin(), neighbors.end());
            auto last = std::unique(neighbors.begin(), neighbors.end());
            neighbors.erase(last, neighbors.end());
            
            adjacencyList[i] = neighbors;
        }
    }

    void findAllPaths() {
        dfs(0, vertices - 1);
        
        if (allPaths.empty()) {
            std::cout << "0" << std::endl;
            return;
        }
        std::sort(allPaths.begin(), allPaths.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            for (size_t i = 0; i < std::min(a.size(), b.size()); i++) {
                if (a[i] != b[i]) {
                    return a[i] < b[i];
                }
            }
            return a.size() < b.size();
        });

        for (const auto& path : allPaths) {
            for (size_t i = 0; i < path.size(); i++) {
                std::cout << path[i];
                if (i < path.size() - 1) {
                    std::cout << "->";
                }
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    int v, e;
    std::cin >> v >> e;

    Graph graph(v, e);
    graph.readGraph();
    graph.findAllPaths();

    return 0;
}