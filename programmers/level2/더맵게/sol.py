# def solution(scoville, K):
#     answer = 0
#     if set(scoville) == {0}:
#         answer = -1
#     else: 
#         while min(scoville) < K:
#             scoville.sort()
#             scoville.append(scoville[0] + 2*scoville[1])
#             scoville.pop(0)
#             scoville.pop(0)
#             answer += 1
#     return answer

def solution(scoville, K):
    answer = 0
    if set(scoville) == {0}:
        answer = -1
    else:
        scoville.sort() 
        while min(scoville) < K:
            if (scoville[0] + 2*scoville[1]) >= K:
                scoville.pop(0)
                scoville.pop(0)
            else:
                scoville.sort()
                scoville.append(scoville[0] + 2*scoville[1])
                scoville.pop(0)
                scoville.pop(0)
            
            answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))