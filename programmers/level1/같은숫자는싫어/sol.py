def solution(arr):
    answer = []
    stack = ['a']
    for i in arr:
        if i != stack[-1]:
            answer.append(i)
            stack.append(i)
    return answer

print(solution([1,1,3,3,0,1,1]))