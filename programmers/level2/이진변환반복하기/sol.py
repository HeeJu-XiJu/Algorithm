def solution(s):
    num = s
    count = 0
    count2 = 0
    while num != '1':
        temp = ''
        for n in num:
            if n == '1':
                temp += n
            else:
                count2 += 1

        length = len(temp)
        
        num = bin(length)[2:]
        count += 1
    return [count, count2]

print(solution("110010101001"))