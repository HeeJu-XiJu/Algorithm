def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        a, b = parts[i]
        answer += my_strings[i][a:b+1]
    return answer

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))