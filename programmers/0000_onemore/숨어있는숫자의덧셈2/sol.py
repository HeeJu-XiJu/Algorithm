def solution(my_string):
    import re
    answer_list= re.findall(r'[0-9]+', my_string)
    answer = 0
    for i in answer_list:
        answer += int(i)
    
    return answer

print(solution("aAb1B2cC34oOp"))