def solution(my_string):
    my_list = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    for char in my_string:
        if char not in my_list:
            answer += char

    return answer

print(solution("bus"))