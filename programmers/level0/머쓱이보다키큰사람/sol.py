def solution(array, height):
    sort_array = sorted(array, reverse = True)
    answer = 0
    for i in range(len(array)):
        if sort_array[i] > height:
            answer += 1
    return answer

print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))