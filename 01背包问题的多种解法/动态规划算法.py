import time
def k(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


weights = [2, 3, 4, 5]
values =  [3, 4, 5, 6]
for i in range(1000000):
    weights.append(i%29+1)
    values.append(i%23+1)
capacity = 50

start_time = time.time()
optimal_value_dp = k(weights, values, capacity)
end_time = time.time()
print(f"动态规划得到的最优解值: {optimal_value_dp}")
execution_time_dp = end_time - start_time
print(f"动态规划求解时间: {execution_time_dp:.6f} 秒")
