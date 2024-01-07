# from itertools import permutations

# def solution(numbers, target):
#     neg_numb = numbers + [(-num) for num in numbers]
#     permlist = set(permutations(neg_numb, len(numbers)))
#     print(permlist)

#     count = 0
#     for perm in permlist:
#         if sum(perm) == target:
#             count += 1
#     return count

def solution(numbers, target):
    count = 0

    def DFS(idx, value):
        nonlocal count
        if idx == len(numbers) and value == target:
            count += 1
            return
        elif idx == len(numbers):
            return
        
        DFS(idx+1, value+numbers[idx])
        DFS(idx+1, value-numbers[idx])

    DFS(0, 0)
    return count

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))


## 다른 풀이
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)