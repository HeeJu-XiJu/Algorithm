import sys
sys.stdin = open('input.txt')

N = int(input())

dfslist = []

def dfs():
    if len(dfslist) == N:
        print(' '.join(map(str, dfslist)))
        return
    for i in range(1, N+1):
        if i not in dfslist:
            dfslist.append(i)
            dfs()
            dfslist.pop()
dfs()
