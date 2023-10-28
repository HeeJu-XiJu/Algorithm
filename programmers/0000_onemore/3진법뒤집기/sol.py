def convert(num, base):
    answer = ''
    while num > 0:
        num, mod = divmod(num, base)
        answer += str(mod)
    return answer[::-1]


def solution(n):
    answer = int(convert(n, 3)[::-1], 3)
    return answer

print(solution(45))