def solution(n):
    answer_list = []
    for a in range(1, N+1):
        if N % a == 0:
            answer_list.append(a)
    return len(answer_list)

print(solution(100))