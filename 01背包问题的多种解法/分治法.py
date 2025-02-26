import time
def k(weights, values, capacity, n,start_time):
    t=time.time()
    tt=t- start_time
    if tt>10:
        print("超时")
        return -1

    if n == 0 or capacity == 0:
        return 0

    if weights[0] <= capacity:
        key=k(weights[1:], values[1:], capacity - weights[0], n - 1,start_time)
        if key == -1:
            return -1
        include_first = values[0] + key
    else:
        include_first = 0

    exclude_first = k(weights[1:], values[1:], capacity, n - 1,start_time)
    if exclude_first == -1:
        return -1
    return max(include_first, exclude_first)



weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
for i in range(20):
    weights.append(i%29+1)
    values.append(i%23+1)
capacity = 50
n = len(weights)  # 物品的数量
start_time = time.time()
max_value = k(weights, values, capacity, n,start_time)
end_time = time.time()
print(f"背包内物品的最大总价值为: {max_value}")
execution_time_dp = end_time - start_time
print(f"分治法求解时间: {execution_time_dp:.6f} 秒")