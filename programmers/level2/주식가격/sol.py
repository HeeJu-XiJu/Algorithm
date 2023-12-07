# from collections import deque

# def solution(prices):
#     answer = []
#     prices = deque(prices)

#     while len(prices) > 0:
#         price = prices.popleft()
#         second = len(prices)
#         for s in range(len(prices)):
#             if price > prices[s]:
#                 second = s+1
#                 break
#         answer.append(second)
            
#     return answer


# from collections import deque

# def solution(prices):
#     answer = []
#     prices = deque(prices)

#     while len(prices) > 0:
#         price = prices.popleft()
#         second = len(prices)
#         for p in prices:
#             if price > p:
#                 second = prices.index(p)+1
#                 break
#         answer.append(second)
            
#     return answer

# print(solution([1, 2, 3, 2, 3]))



# 다른 풀이
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])
        # print(answer, stack)
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

# print(solution([1, 2, 3, 2, 3]))