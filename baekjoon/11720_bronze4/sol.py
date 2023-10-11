import sys
sys.stdin = open('input.txt')

T = int(input())
a = input()
answer = 0

for num in a:
    answer += int(num)

print(answer)