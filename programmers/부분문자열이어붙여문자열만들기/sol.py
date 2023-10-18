def solution(my_strings, parts):
    for i in range(len(parts)):
        my_strings[i][parts[i, 0]:parts[i, 1]]
    answer = ''
    return answer

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))