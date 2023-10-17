def solution(numlist, n):
    answer = []
    if n in numlist:
        answer.append(n)
    
    for i in range(1, 10001):
        if n + i in numlist:
            answer.append(n)
        elif n - i in numlist:
            answer.append(n)
    
    return answer

    print(solution([1, 2, 3, 4, 5, 6], 4))
