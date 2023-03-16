from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    ing = deque(0 for i in range(bridge_length))
    check = 0
    while ing:
        answer += 1
        check -= ing.popleft()
        if truck_weights: 
            if check + truck_weights[0] <= weight:
                ing.append(truck_weights.popleft())
                check += ing[-1]
            else:
                ing.append(0)
    return answer