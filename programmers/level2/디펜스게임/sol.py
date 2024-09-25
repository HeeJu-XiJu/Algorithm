# def solution(n, k, enemy):
#     maxenemy = 0
#     answer = 0
#     removeidx = 0
#     for i in range(len(enemy)):
#         maxenemy += enemy[i]
#         if maxenemy <= n:
#             answer += 1
#         else:
#             while maxenemy > n:
#                 if k != 0 and removeidx != i:
#                     removeidx = enemy[removeidx:i].index(max(enemy[removeidx:i]))
#                     maxenemy -= enemy[removeidx]
#                     k -= 1
#                     answer += 1
#                 elif k != 0 and removeidx == i:
#                     maxenemy -= enemy[i]
#                     k -= 1
#                     answer += 1    
#                 else:
#                     break
#     return answer

from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)
        sumEnemy += e
        if sumEnemy > n:
            if k == 0: break
            sumEnemy += heappop(heap) 
            k -= 1
        answer += 1
    return answer

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))