import sys
sys.stdin = open('input.txt')

N = int(input())

for _ in range(N):
    M, N, x, y = map(int, input().split(' '))

    for i in range(x, M*N+1, M):
        if (i - x) % M == 0 and (i - y) % N == 0:
            print(i)
            break
    else:
        print(-1)