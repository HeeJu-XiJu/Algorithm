def solution(n, control):
    answer = n
    for i in control:
        if i == 'w':
            answer += 1
        elif i == 's':
            answer -= 1
        elif i == 'd':
            answer += 10
        else :
            answer -= 10
    return answer

print(solution(0, "wsdawsdassw"))

# 다른 풀이
# dictionary 활용
def solution(n, control):
    answer = n
    dic = {
        'w' : 1,
        's' : -1,
        'd' : 10,
        'a' : -10,
    }
    for i in control:
        answer += dic[i]
    return answer
