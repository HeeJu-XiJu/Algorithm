def solution(array):
    my_list = []
    max_key = []

# 각 인수 count 구하기
    for number in array:
        count_array = array.count(number)
        my_list.append([number, count_array])
        my_dict = dict(my_list)

# count값 중 max 찾기
    for a, b in my_dict.items():
        if max(my_dict.values()) == b:
            max_key.append(a)

# 중복 최빈값 조건
    if len(max_key) != 1:
        answer = -1
    else:
        answer = max_key[0]

    return answer

print(solution([1, 2, 3, 3, 3, 4]))