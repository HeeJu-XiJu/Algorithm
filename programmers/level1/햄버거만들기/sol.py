# def solution(ingredient):
#     answer = -1
#     if [1, 2, 3, 1] in ingredient:
#         return 0
#     return answer


def solution(ingredient):
    num = 0
    answer = 0
    while num < len(ingredient)-3:
        if ingredient[num] == 1 and ingredient[num+1] == 2 and ingredient[num+2] == 3 and ingredient[num+3] == 1:
            ingredient.pop(num)
            ingredient.pop(num)
            ingredient.pop(num)
            ingredient.pop(num)
            answer += 1
            num = 0
        num += 1
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))