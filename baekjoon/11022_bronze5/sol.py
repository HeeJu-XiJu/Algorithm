import sys
sys.stdin = open('input.txt')

T = int(input())
n = 0

for number in range(1, T+1):
    a, b = list(map(int,input().split()))
    n += 1
    print(f'Case #{n}: {a} + {b} = {a + b}')