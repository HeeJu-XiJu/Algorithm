def solution(new_id):
    answer = new_id

    #1
    answer = new_id.lower()
    
    #2
    removelist = '~!@#$%^&*()=+[{]}:?,<>/'
    for i in answer:
        if i in removelist:
            answer = answer.replace(i, '')

    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 다른 풀이
    # answer.strip(.)
    #4 
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
        
    #5
    if len(answer) == 0:
        answer = 'a'

    #6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]

    #7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution(""))