def solution(my_string, n):
    return my_string[len(my_string)-n:]

print(solution("ProgrammerS123", 11))

# 다른풀이
my_string[-n:]