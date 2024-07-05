import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
S = set()
N = int(input())

for _ in range(N):
    mlist = list(input().split())
    A = mlist[0]
    if A == 'add':
        x = int(mlist[1])
        S.add(x)
    elif A == 'remove':
        x = int(mlist[1])
        if x in S:
            S.remove(x)
    elif A == 'check':
        x = int(mlist[1])
        if x not in S:
            print(0)
        else:
            print(1) 
    elif A == 'toggle':
        x = int(mlist[1])
        if x not in S:
            S.add(x)
        else:
            S.remove(x)
    elif A == 'all':
        S = set([i for i in range(1, 21)])
    else:
        S = set()