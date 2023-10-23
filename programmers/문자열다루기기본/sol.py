def solution(s):
    answer = 0
    try:
        if len(s) == 4 or len(s) == 6:
            for char in s:
                if type(int(char)) == int:
                    answer = True
        else:
            answer = False
    except:
        answer = False
    return answer

print(solution("10X010"))