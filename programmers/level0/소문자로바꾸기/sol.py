def solution(myString):
    answer = ''
    for char in myString:
        if char.isupper() == True:
            answer += char.lower()
        else:
            answer += char
    return answer


print(solution("aBcDeFg"))