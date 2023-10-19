def solution(array):
    number = ''
    for i in array:
        number += str(i)

    answer = number.count('7')
    return answer

print(solution([7, 77, 17]))