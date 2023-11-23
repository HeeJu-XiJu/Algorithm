def solution(ing):
    count = 0
    stack = []
    num = 0
    while num < len(ing):
        stack.append(ing[num])
        num += 1
        if len(stack) >= 4 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            count += 1
    return count


# def solution(ing):
#     count = 0
#     stack = []
#     for i in ing:
#         stack += [i]
#         if len(stack) >= 4 and stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
#             stack.pop()
#             stack.pop()
#             stack.pop()
#             stack.pop()
#             count += 1
#     return count

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))