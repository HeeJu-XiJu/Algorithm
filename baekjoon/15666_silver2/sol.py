import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split(' '))
mlist = sorted(list(map(int, input().split(' '))))

dfslist = []

def dfs(s):
    if len(dfslist) == M:
        print(' '.join(map(str, dfslist)))
        return
    num = 0
    for i in range(s, N):
        if num != mlist[i]:
            dfslist.append(mlist[i])
            num = mlist[i]
            dfs(i)
            dfslist.pop()

dfs(0)