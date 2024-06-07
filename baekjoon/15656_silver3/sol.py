import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split(' '))
mlist = list(map(int, input().split(' ')))
mlist.sort()

dfslist = []
def dfs():
    if len(dfslist) == M:
        print(' '.join(map(str, dfslist)))
        return

    for i in mlist:
        dfslist.append(i)
        dfs()
        dfslist.pop()

dfs()