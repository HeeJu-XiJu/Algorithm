def solution(my_string):
    answer = ''
    for char in my_string:
        if char in answer:
            pass
        else :
            answer += char

    return answer

print(solution("people"))