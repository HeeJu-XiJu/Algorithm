def solution(s):
    answer2 = ''
    for char in s:
        if s.count(char) == 1:
            answer2 += char
    answer2 = sorted(answer2)
    
    answer = ''
    for char in answer2:
        answer += char
        
    return answer

print(solution("abcabcadc"))