def solution(s):
    answer = 0
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
            continue
        a = stack.pop()
        if a == i:
            continue
        else:
            stack.append(a)
            stack.append(i)

    if len(stack) == 0:
        answer = 1
    return answer

print(solution('cdcd'))