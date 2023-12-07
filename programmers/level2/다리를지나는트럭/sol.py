# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     ing = []
#     count = bridge_length
#     for truck in truck_weights:
#         if len(ing) == 0 :
#             answer += bridge_length
#             ing.append(truck)
#         elif sum(ing) + truck <= weight:
#             answer += 1
#             ing.append(truck)
#         elif sum(ing) + truck > weight:
#             while len(ing) != 0 and sum(ing) + truck > weight:
#                 ing.pop(0)
#                 count = bridge_length - len(ing)
#             answer += count
#             ing.append(truck)
#         print(answer, ing, count)
#     return answer+1


# def solution(bridge_length, weight, truck_weights):
#     ing = []
#     ing_time = []
#     time = 0
#     for truck in truck_weights:
#         if len(ing) == 0:
#             ing.append(truck)
#             ing_time.append(time+bridge_length)
#         elif sum(ing) + truck <= weight:
#             ing.append(truck)
#             ing_time.append(time+1)
#         elif sum(ing) + truck > weight:
#             while sum(ing) + truck > weight:
#                 ing.pop(0)
#                 time = ing_time.pop(0)
#             ing.append(truck)
#             ing_time.append(time+bridge_length)
#         time = ing_time[-1]
#     return time+1


def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[-1::-1]
    
    time = 0
    ing = []
    ing_time = []
    finish = []
    while len(truck_weights) > 0:
        time += 1
        if len(ing_time) != 0 and ing_time[0] == time:
            ing_time.pop(0)
            finish.append(ing.pop(0))

        truck = truck_weights.pop()
        if sum(ing) + truck <= weight:
            ing.append(truck)
            ing_time.append(time + bridge_length)
        elif sum(ing) + truck > weight:
            truck_weights.append(truck)
    
    return ing_time[-1]

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
print(solution(10, 100, [50, 30, 10, 10, 30, 10, 40]))


# 다른 풀이
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step