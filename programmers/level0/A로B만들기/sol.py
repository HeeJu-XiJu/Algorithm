def solution(before, after):
    before_list = []
    after_list = []
    for char in before:
        before_list.append(char)
    for char in after:
        after_list.append(char)
    
    if sorted(before_list) == sorted(after_list):
        answer = 1
    else :
        answer = 0

    return answer

print(solution('olleh', 'hello'))