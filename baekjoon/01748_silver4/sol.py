import sys
sys.stdin = open('input.txt')

N = int(input())
num = 0

n = 0
for i in range(1, 10):
    if N // (10 ** i) == 0:
        n = i
        break

for i in range(1, n):
    num += 9 * (10 ** (i-1)) * i

print(num + ((N + 1 - 10 ** (n-1)) * n))