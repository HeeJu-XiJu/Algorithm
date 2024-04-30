import sys
sys.stdin = open('input.txt')

N = int(input())

primelist = [False, False] + [True] * (N-1)

for i in range(2, N+1):
    if primelist[i]:
        for j in range(i+i, N+1, i):
            primelist[j] = False

while N >= 2:
    for i in range(2, N+1):
        if primelist[i] and N % i == 0:
            print(i)
            N = N // i
            break