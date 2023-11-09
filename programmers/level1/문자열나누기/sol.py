def solution(s):
    stack1 = 0
    stack2 = 0
    answer = 0
    num = 0
    for i in s:
        if stack1 == 0:
            num = i
        if i == num:
            stack1 += 1
        else:
            stack2 += 1
        if stack1 != 0 and stack1 == stack2:
            answer +=1
            stack1 = 0
            stack2 = 0
    if stack1 != 0:
        answer +=1
    
    return answer


print(solution("banana"))