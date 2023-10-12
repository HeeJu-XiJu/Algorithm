import sys
sys.stdin = open('input.txt')

a = input()
answer = 1

for char in a:
    if char == ' ':
        answer += 1

if a[0] == ' ' and a[-1] == ' ':
    answer -= 2
elif a[-1] == ' ':
    answer -= 1
elif a[0] == ' ' :
    answer -= 1

print(answer)