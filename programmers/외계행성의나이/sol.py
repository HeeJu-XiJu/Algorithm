def solution(age):
    answer = ''
    for num in str(age):
        answer += chr(ord(num) + 49)
    return answer

print(solution(23))
