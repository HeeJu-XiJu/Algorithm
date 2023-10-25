def solution(s):
    answer = []
    stack = []
    for i in range(len(s)):
        if s[i] not in stack:
            answer.append(-1)
            stack.append(s[i])
        else:
            for j in range(i-1,-1,-1): # (i-1, 0, -1)로 하면 0 포함안됨
                if s[j] == s[i]:
                    answer.append(i-j)
                    break
    return answer

print(solution('programmers'))


def solution(s):
    answer = []
    stack = []
    m = []
    for i in range(len(s)):
        if s[i] not in stack:
            answer.append(-1)
            stack.append(s[i])
        else:
            for j in range(i):
                if s[i] == s[j]:
                    m.append(i - j)
            answer.append(min(m))
            m = []
    return answer

print(solution('programmers'))
                

