from itertools import combinations

# def solution(clothes):
#     mdict = {}
#     for cloth in clothes:
#         mdict[cloth[1]] = mdict.get(cloth[1], 0) + 1
    
#     cloth = list(mdict.values())

#     answer = 0
#     for num in cloth:
#         answer += num

#     for num in range(2, len(cloth)+1):
#         combs = list(combinations(cloth, num))
#         for comb in combs:
#             sum = 1
#             for num in comb:
#                 sum *= num
#         answer += sum 

#     return answer


def solution(clothes):
    mdict = {}
    for cloth in clothes:
        mdict[cloth[1]] = mdict.get(cloth[1], 0) + 1
    
    answer = 1
    for num in mdict.values():
        answer *= (num+1)
    
    return answer-1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))