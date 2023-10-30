def solution(s):
    answer = s[0].upper()

    for i in range(1, len(s)):
        if s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer

# str(숫자)도 upper 가능, 결과값이 변하진 않음