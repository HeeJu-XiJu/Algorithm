def solution(numbers, hand):
    keypad = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']
    answer = ''
    hand_L = '*'
    hand_R = '#'
    for num in numbers:
        if num in {1, 4, 7}:
            answer += 'L'
            hand_L = num
        elif num in {3, 6, 9}:
            answer += 'R'
            hand_R = num
        else: 
            L = abs(keypad.index(num) - keypad.index(hand_L)) // 3 + abs(keypad.index(num) - keypad.index(hand_L)) % 3
            R = abs(keypad.index(num) - keypad.index(hand_R)) // 3 + abs(keypad.index(num) - keypad.index(hand_R)) % 3
            if L < R:
                answer += 'L'
                hand_L = num
            elif L > R:
                answer += 'R'
                hand_R = num
            else:
                if hand == 'right':
                    answer += 'R'
                    hand_R = num
                else:
                    answer += 'L'
                    hand_L = num

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))