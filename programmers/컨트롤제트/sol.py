def solution(s):
    answer = 0
    s = list(map(str, s.split()))
    for i in range(len(s)):
        if s[i] == "Z":
            answer -= int(s[i-1])
        else :
            answer += int(s[i])

    return answer

print(solution("1 2 Z 3"))