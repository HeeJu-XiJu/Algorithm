def solution(numbers, direction):
    answer = numbers
    if direction == "left":
        first = answer[0]
        for i in range(len(numbers)-1):
            answer[i] = answer[i+1]
        answer[-1] = first
    else:
        last = answer[-1]
        for i in range(len(numbers)-1):
            answer[-i-1] = answer[-i-2]
        answer[0] = last
    return answer

print(solution([1, 2, 3], "right"))