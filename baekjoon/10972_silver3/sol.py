import sys
sys.stdin = open('input.txt')

N = int(input())
numlist = list(map(int, input().split(' ')))

for i in range(N-1, 0, -1):
    if numlist[i-1] < numlist[i]:
        for j in range(N-1, 0, -1):
            if numlist[i-1] < numlist[j]:
                numlist[i-1], numlist[j] = numlist[j], numlist[i-1]
                numlist = numlist[:i] + sorted(numlist[i:])
                for i in numlist:
                    print(i, end=' ')
                exit()
print(-1)