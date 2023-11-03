def solution(strings, n):
    answer = []
    mlist = []
    for i, j in enumerate(strings):
        mlist.append([j[n], i])

    stack = []
    for k in sorted((mlist)):
        if len(stack) == 0:
            stack.append(strings[k[1]])
        elif k[0] != stack[0][n]:
            for i in sorted(stack):
                answer.append(i)
            stack = [strings[k[1]]]
        elif k[0] == stack[0][n]:
            stack.append(strings[k[1]])
    
    if len(answer) != len(strings):
        for i in sorted(stack):
            answer.append(i)

    return answer

print(solution(["sun", "bed", "car"], 1))