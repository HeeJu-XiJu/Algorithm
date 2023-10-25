def solution(s):
    answer = 0
    if s[0] == '-' :
        answer = -int(s[1:])
    elif s[0] == '+':
        answer = int(s[1:])
    else:
        answer = int(s)
    return answer

# int는 부호 -, +를 인식함