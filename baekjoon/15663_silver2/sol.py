import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split(' '))
mlist = list(map(int, input().split(' ')))
mlist.sort()

visited = [False] * N
dfslist = []
def dfs():
    if len(dfslist) == M:
        print(' '.join(map(str, dfslist)))
        return
    remember = 0
    for i in range(N):
        if not visited[i] and remember != mlist[i]:
            visited[i] = True
            dfslist.append(mlist[i])
            remember = mlist[i]
            dfs()
            visited[i] = False
            dfslist.pop()

dfs()