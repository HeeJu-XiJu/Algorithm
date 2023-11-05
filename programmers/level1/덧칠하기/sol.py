# def solution(n, m, section):
#     answer = 0
#     for i in range(len(section)):
#         if section[i] != 'a':
#             answer += 1
#             for j in range(1, m):
#                 if section[i]+j in section:
#                     section[section.index(section[i]+j)] = 'a'
#             section[i] = 'a'

#     return answer

# def solution(n, m, section):
#     answer = 0
#     while len(section) != 0:
#         answer += 1
#         for j in range(1, m):
#             if section[0]+j in section:
#                     section.remove(section[0]+j)
#         section.pop(0)

#     return answer

def solution(n, m, section):
    answer = 0
    while len(section) != 0:
        answer += 1
        while len(section) > 1 and section[1] <= section[0]+m-1:
            section.pop(1)
        section.pop(0)

    return answer

print(solution(8, 4, [2, 3, 6]))