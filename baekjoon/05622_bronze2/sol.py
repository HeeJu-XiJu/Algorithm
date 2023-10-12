import sys
sys.stdin = open('input.txt')

a = input()
answer = 0

list_2 = ['A', 'B', 'C', 3]
list_3 = ['D', 'E', 'F', 4]
list_4 = ['G', 'H', 'I', 5]
list_5 = ['J', 'K', 'L', 6]
list_6 = ['M', 'N', 'O', 7]
list_7 = ['P', 'Q', 'R', 'S', 8]
list_8 = ['T', 'U', 'V', 9]
list_9 = ['W', 'X', 'Y', 'Z', 10]

for char in a:
    if char in list_2:
        answer += list_2[-1]
    elif char in list_3:
        answer += list_3[-1]
    elif char in list_4:
        answer += list_4[-1]
    elif char in list_5:
        answer += list_5[-1]
    elif char in list_6:
        answer += list_6[-1]
    elif char in list_7:
        answer += list_7[-1]
    elif char in list_8:
        answer += list_8[-1]
    else:
        answer += list_9[-1]

print(answer)
