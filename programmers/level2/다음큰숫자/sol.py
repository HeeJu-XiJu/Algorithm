def solution(n):
    num1 = str(bin(n))
    count1 = num1.count('1')

    num2 = n + 1
    while str(bin(num2)).count('1') != count1:
        num2 += 1

    return num2

print(solution(78))