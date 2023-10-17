def solution(my_string):
    answer = ''
    for char in my_string:
        if char.islower() == True:
            answer += char.upper()
        else :
            answer += char.lower()
    return answer

print(solution("cccCCC"))