import sys
sys.stdin = open('input.txt')

n = int(input())
result = 0

for number in range(1, n+1):
    result += number

print(result)