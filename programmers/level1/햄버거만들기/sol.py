# def solution(ingredient):
#     answer = -1
#     if [1, 2, 3, 1] in ingredient:
#         return 0
#     return answer


def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4:
            if stack[len(stack)-4:] == [1, 2, 3, 1]:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer += 1
        
    return answer


# def solution(ingredient):
#     stack = ''
#     answer = 0
#     for i in ingredient:
#         stack += str(i)
        
#         if len(stack) >= 4:
#             if stack[len(stack)-4:] == '1231':
#                 stack = stack[:len(stack)-4]
#                 answer += 1
    
#     return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))