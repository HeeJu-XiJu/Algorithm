import sys
sys.stdin = open('input.txt', encoding='utf-8')

char1 = input()
char2 = input()

# if char1 == '가위' and char2 == '보':
#     print('Result : Man1 Win!')
# elif char1 == '바위' and char2 == '가위':
#     print('Result : Man1 Win!')
# elif char1 == '보' and char2 == '바위':
#     print('Result : Man1 Win!')
# elif char1 == char2:
#     print('Result : Draw')
# else:
#     print('Result : Man2 Win!')


rcp = ['가위', '바위', '보']

char1_idx = rcp.index(char1)
char2_idx = rcp.index(char2)

result = char1_idx - char2_idx

if result == 0:
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    print(f'Result : Man{result+3} Win!')