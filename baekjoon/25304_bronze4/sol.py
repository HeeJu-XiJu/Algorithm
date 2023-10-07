import sys
sys.stdin = open('input.txt')

total = int(input())
number = int(input())
result = 0

for price in range(1, number + 1):
    a, b = list(map(int,input().split()))
    result += (a * b)

if total == result:
    print('Yes')
else:
    print('No')