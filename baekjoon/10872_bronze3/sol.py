import sys
sys.stdin = open('input.txt')

n = int(input())
answer = 1

while n != 1 and n != 0:
    answer *= n
    n -= 1

print(answer)