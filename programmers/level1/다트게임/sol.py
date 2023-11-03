def solution(dartResult):
    answer = 0
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(len(dartResult)):
        try:
            if type(int(dartResult[i])) == int:
                    num2 = num1
                    num1 = int(dartResult[i])

            if type(int(dartResult[i])) == int and type(int(dartResult[i-1])) == int:
                    num2 = num3
                    num1 = 10
                
        except:
            if dartResult[i] == 'S':
                num1 = num1 ** 1
                answer += num1
            elif dartResult[i] == 'D':
                num1 = num1 ** 2
                answer += num1
            elif dartResult[i] == 'T':
                num1 = num1 ** 3
                answer += num1
            elif dartResult[i] == '#':
                num1 *= (-1)
                answer += num1 * 2
            elif dartResult[i] == '*':
                if num2 == 0:
                    answer += num1
                    num1 *= 2
                    num2 = num1 * 2
                else:
                    answer += num1 + num2
                    num1 *= 2
                    num2 *= 2
            num3 = num2
    return answer

print(solution('1S*2T*3S'))

# 다른 풀이
dartResult.replace('10', 'k')
10을 replace하여 풀이