def solution(d, budget):
    answer = 0
    total = 0
    for i in sorted(d):
        if total+i <= budget:
            answer += 1
            total += i
        else:
            break
    return answer

print(solution([1, 3, 2, 5, 4], 9))

# 다른 풀이
def solution(d, budget):
    d.sort()
    while sum(d) > budget:
        d.pop()
    return len(d)