def solution(n):
    my_list = []
    for i in str(n):
        my_list.append(i)

    my_list = sorted(my_list, reverse = True)
    answer = int(''.join(my_list))

    return answer

print(solution(118372))

# 다른 풀이
# my_list = list(str(n))으로 만들 수 있음