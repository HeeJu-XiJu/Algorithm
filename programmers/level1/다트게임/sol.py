def solution(dartResult):
    answer = 0
    num1 = 0
    num2 = 0
    for i in dartResult:
        try:
            if type(int(i)) == int:
                num1 = int(i)
        except:
            if i != '#' or i != '*':
                if i == 'S':
                    num1 = num1 ** 1
                elif i == 'D':
                    num1 = num1 ** 2
                elif i == 'T':
                    num1 = num1 ** 3
                    
                answer += num1
                num2 = num1

            if i == '#':
                num1 *= (-1)
                answer += num1 * 2
                num2 = num1
            else:
                if num2 == 0:
                    answer += num1
                    num2 = num1
                else:
                    answer += num2
        print(num1)
    return answer


print(solution('1S2D*3T'))