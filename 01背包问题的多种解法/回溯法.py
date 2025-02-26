import time


def k(weights, values, capacity, start_time,i=0, current_weight=0, current_value=0,best_value=float('-inf')):
    t=time.time()
    tt=t-start_time
    if(tt>10):
        print("超时")
        return -1
    if i == len(weights) or current_weight == capacity:
        return current_value

    key=k(weights, values, capacity, start_time,i + 1, current_weight, current_value,best_value)
    if(key==-1):
        return -1
    exclude =key

    best_value= max(exclude, best_value)

    remaining_items = [(values[j] / weights[j], j, values[j], weights[j]) for j in range(i, len(weights))]
    remaining_items.sort(reverse=True)
    upper_bound = current_value
    for _, j, v, w in remaining_items:
        if current_weight + w <= capacity:
            upper_bound += v
        else:
            upper_bound += (capacity - current_weight) * (v / w)
            break

    if upper_bound <= best_value:
        return best_value

    include = 0
    if current_weight + weights[i] <= capacity:
        key =k(weights, values, capacity,start_time, i + 1, current_weight + weights[i],current_value + values[i], best_value)
        if (key == -1):
            return -1
        include = key
    best_value = max(exclude, include)
    return best_value

weights = [2, 3, 4, 5]
values =  [3, 4, 5, 6]
for i in range(20):
    weights.append(i%29+1)
    values.append(i%23+1)

capacity = 50
start_time = time.time()
optimal_value_backtrack = k(weights, values, capacity,start_time )
end_time = time.time()
print(f"回溯法得到的最优解值: {optimal_value_backtrack}")
execution_time_backtrack = end_time - start_time
print(f"回溯法求解时间: {execution_time_backtrack:.6f} 秒")
