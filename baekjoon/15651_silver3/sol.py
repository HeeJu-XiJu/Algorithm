import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split(' '))

mlist = []

def dfs():
    if len(mlist) == M:
        print(' '.join(map(str, mlist)))
        return
    
    for i in range(1, N+1):
        mlist.append(i)
        dfs()
        mlist.pop()

dfs()