def solution(code):
    now = False
    idx = 0
    answer = ''
    while idx < len(code):
        if code[idx] == '1':
            now = not(now)
            idx += 1
        elif now == False and idx % 2 == 0:
            answer += code[idx]
            idx += 1
        elif now == True and idx % 2 != 0:
            answer += code[idx]
            idx += 1
        else:
            idx += 1
    if answer == '':
        answer = 'EMPTY'

    return answer

print(solution("abc1abc1abc"))