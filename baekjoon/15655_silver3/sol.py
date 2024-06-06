import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split(' '))
mlist = list(map(int, input().split(' ')))
mlist.sort()

dfslist = []
def dfs(s):
    if len(dfslist) == M:
        print(' '.join(map(str, dfslist)))
        return
    for i in range(s, len(mlist)):
        if mlist[i] not in dfslist:
            dfslist.append(mlist[i])
            dfs(i+1)
            dfslist.pop()

dfs(0)