def solution(array, n):
    sort_array = sorted(array)
    answer = 0
    ab = 100
    for i in sort_array:
        if abs(i-n) < ab:
            answer = i
            ab = abs(i-n)
    return answer

print(solution([3, 10, 28], 20))