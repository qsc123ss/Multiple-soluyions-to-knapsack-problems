import time
def k(weights, values, capacity):
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    total_weight = 0
    total_value = 0

    for value, weight in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
        else:
            break

    return total_value

weights = [2, 3, 4, 5]
values =  [3, 4, 5, 6]
for i in range(1000000):
    weights.append(i%29+1)
    values.append(i%23+1)

capacity = 50
start_time = time.time()
optimal_value_greedy = k(weights, values, capacity)
end_time = time.time()
print(f"贪心算法得到的最优解值: {optimal_value_greedy}")
execution_time_greedy = end_time - start_time
print(f"贪心算法求解时间: {execution_time_greedy:.6f} 秒")
