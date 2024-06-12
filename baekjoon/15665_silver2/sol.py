import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split(' '))
mlist = sorted(list(map(int, input().split(' '))))
mdict = {}

for i in mlist:
    mdict[i] = 0

mlist = list(mdict)
dfslist = []

def dfs():
    if len(dfslist) == M:
        print(' '.join(map(str, dfslist)))
        return
    for i in range(len(mlist)):
        dfslist.append(mlist[i])
        dfs()
        dfslist.pop()

dfs()