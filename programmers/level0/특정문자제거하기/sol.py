def solution(my_string, letter):
    answer = ''
    for char in my_string:
        if char not in letter:
            answer += char
    
    return answer

print(solution("abcdef", "f"))