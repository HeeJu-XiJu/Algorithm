def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        num = 0
        if i ** 0.5 % 1 == 0:
            num = 1
            for j in range(1, int(i**0.5)):
                if i % j == 0:
                    num += 2
        else:
            for j in range(1, int(i**0.5+1)):
                if i % j == 0:
                    num += 2
        if num > limit:
            answer += power
        else:
            answer += num
    return answer

print(solution(5, 3, 2))