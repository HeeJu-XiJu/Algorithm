def solution(str1, str2):
    answer = 2
    for i in range(0, len(str1) - len(str2) + 1):
        if str1[i:i+len(str2)] == str2:
            answer = 1
        
    return answer

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))