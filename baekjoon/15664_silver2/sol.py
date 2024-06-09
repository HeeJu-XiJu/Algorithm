import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split(' '))
mlist = sorted(list(map(int, input().split(' '))))

visited = [False] * N
dfslist = []

def dfs(s):
    if len(dfslist) == M:
        print(' '.join(map(str, dfslist)))
        return
    remember = 0
    for i in range(s, N):
        if not visited[i] and remember != mlist[i]:
            visited[i] = True
            dfslist.append(mlist[i])
            remember = mlist[i]
            dfs(i+1)
            dfslist.pop()
            visited[i] = False

dfs(0)