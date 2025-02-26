import heapq
import  time

def bound(weights, values, capacity, i, current_weight, current_value):
    remaining_items = sorted(zip(values[i:], weights[i:]), key=lambda x: x[0] / x[1], reverse=True)
    remaining_value = 0
    for value, weight in remaining_items:
        if current_weight + weight <= capacity:
            current_weight += weight
            remaining_value += value
        else:
            break
    return current_value + remaining_value


def k(weights, values, capacity,start_time):
    n = len(weights)
    queue = []
    heapq.heappush(queue, (-0, 0, 0, 0))
    best_value = 0

    while queue:
        t=time.time()
        tt=t-start_time
        if(tt>10):
            print("超时")
            return -1
        current_value, current_weight, i, is_feasible = heapq.heappop(queue)
        current_value = -current_value

        if is_feasible and current_value > best_value:
            best_value = current_value

        if i == n:
            continue
        heapq.heappush(queue, (-current_value, current_weight, i + 1, is_feasible))

        if current_weight + weights[i] <= capacity:
            new_value = current_value + values[i]
            new_bound = bound(weights, values, capacity, i + 1, current_weight + weights[i], new_value)
            if new_bound > best_value:
                heapq.heappush(queue, (-new_value, current_weight + weights[i], i + 1, True))

    return best_value

weights = [2, 3, 4, 5]
values =  [3, 4, 5, 6]
for i in range(100):
    weights.append(i%29+1)
    values.append(i%23+1)
capacity = 50
start_time = time.time()
optimal_value_bnb = k(weights, values, capacity,start_time)
end_time = time.time()
print(f"分支限界法得到的最优解值: {optimal_value_bnb}")
execution_time_bnb = end_time - start_time
print(f"分支限界法求解时间: {execution_time_bnb:.6f} 秒")

