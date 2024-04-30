import sys
sys.stdin = open('input.txt')

N = int(input())

mlist = [0] * 1000001

for i in range(2, N+1):
    mlist[i] = mlist[i-1] + 1

    if i % 2 == 0:
        mlist[i] = min(mlist[i], mlist[i//2] + 1)

    if i % 3 == 0:
        mlist[i] = min(mlist[i], mlist[i//3] + 1)

print(mlist[N])