#ifndef __FORWARDREVERSE_TABLE_H__
#define __FORWARDREVERSE_TABLE_H__

#include "BaseGraph.h"
#include <vector>
#include <algorithm>

class ForwardReverseTable : public BaseGraph
{
private:
    std::vector<int> forwardA; // 正向表A数组
    std::vector<int> forwardB; // 正向表B数组
    std::vector<int> reverseA; // 逆向表A数组
    std::vector<int> reverseB; // 逆向表B数组
    std::vector<int> weights;  // 权重数组

    // 辅助函数：根据边列表构建正向表和逆向表
    void buildTables();

public:
    // 构造函数
    ForwardReverseTable(int vertices, bool directed = false, bool weighted = false);

    // 添加边
    void addEdge(int s, int d, int w = 1);

    // 获取正向表和逆向表
    const std::vector<int> &getForwardA() const;
    const std::vector<int> &getForwardB() const;
    const std::vector<int> &getReverseA() const;
    const std::vector<int> &getReverseB() const;
    const std::vector<int> &getWeights() const;

    // 打印表
    void printTables() const;
};

#endif // __FORWARDREVERSE_TABLE_H__