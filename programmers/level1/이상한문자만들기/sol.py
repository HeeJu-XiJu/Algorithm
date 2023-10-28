def solution(s):
    answer = ''
    num = 0
    for i in s:
        if i == ' ':
            answer += i
            num = 0
        else:
            if num % 2 == 0:
                answer += i.upper()
                num += 1
            elif num % 2 != 0:
                answer += i.lower()
                num += 1
    return answer

print(solution("try hello world"))