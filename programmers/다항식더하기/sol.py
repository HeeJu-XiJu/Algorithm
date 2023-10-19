def solution(polynomial):
    my_list = polynomial.split(' + ')
    x = 0
    number = 0
    for char in my_list:
        if 'x' in char:
            if char == 'x':
                x += 1
            else:
                x += int(char[:-1])
        else:
            number += int(char)

    if x >= 2 and number == 0:
        answer = f'{x}x'
    elif x == 1 and number == 0:
        answer = 'x'
    elif x >= 2 and number != 0:
        answer = f'{x}x + {number}'
    elif x == 1 and number != 0:
        answer = f'x + {number}'
    elif x == 0 and number != 0:
        answer = f'{number}'
    return answer

print(solution("1 + 3 + 111x"))