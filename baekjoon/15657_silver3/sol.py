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
    
        dfslist.append(mlist[i])
        dfs(i)
        dfslist.pop()

dfs(0)