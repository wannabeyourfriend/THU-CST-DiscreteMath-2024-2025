from random import *
from time import clock
#**********  Begin  **********#
#第一题
def minPathCost(cost, i, j):
    m = len(cost)
    n = len(cost[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = cost[0][0]
    # dp initialization
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + cost[0][j]

    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + cost[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + cost[i][j]

    return dp[m - 1][n - 1]

def minPathCost_Memo(cost, i, j, memo):
   return minPathCost(cost, i, j)

def countWays(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return countWays(n - 1) + countWays(n - 2)
def countWays_Memo(n, memo={}):
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo = [0] * (n + 1)
    memo[1] = 1
    memo[2] = 2
    for i in range(3,n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

if __name__=="__main__":
    randseeds = [9, 99, 999, 9999, 99999]
    for trial in range(5):
        seed(randseeds[trial])
        cost = []
        for i in range(10):
            temp = []
            for j in range(10):
                temp.append(randint(1,10))
            cost.append(temp)

        #start = clock()
        print(minPathCost(cost, 9, 9))
        #print(clock() - start)

    print('*' * 20)

    randseeds = [9, 99, 999, 9999, 99999]
    for trial in range(5):
        seed(randseeds[trial])
        cost = []
        for i in range(100):
            temp = []
            for j in range(100):
                temp.append(randint(1, 10))
            cost.append(temp)

        memo = []
        for i in range(100):
            memo.append([0] * 100)
        #start = clock()
        print(minPathCost_Memo(cost, 99, 99, memo))
        #print(clock()-start)

    print('*' * 20)

    for n in range(25,35):
        print(countWays(n))
    print('*' * 20)

    for n in range(90,100):
        print(countWays_Memo(n))




