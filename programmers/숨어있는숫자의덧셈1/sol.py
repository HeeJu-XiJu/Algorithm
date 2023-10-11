def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        try :
            if type(int(my_string[i])) == int:
                answer += int(my_string[i])
        except :
            pass
    return answer

print(solution("aAb1B2cC34oOp"))