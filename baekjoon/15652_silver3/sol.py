import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split(' '))

mlist = []

def dfs(s):
    if len(mlist) == M:
        print(' '.join(map(str, mlist)))
        return
    for i in range(s, N+1):
        mlist.append(i)
        dfs(i)
        mlist.pop()

dfs(1)