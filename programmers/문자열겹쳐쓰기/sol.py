def solution(my_string, overwrite_string, s):
    answer = my_string[:s]
    answer += overwrite_string
    answer += my_string[s+len(overwrite_string):]

    return answer


print(solution("Program29b8UYP", "merS123", 7))