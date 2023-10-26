def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    rev = answer[::-1]
    answer += '0'
    answer += rev
    return answer

print(solution([1, 3, 4, 6]))