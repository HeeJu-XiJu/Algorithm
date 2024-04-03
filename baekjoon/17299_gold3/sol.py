import sys
sys.stdin = open('input.txt')

n = int(input())
mlist = list(map(int, input().split(' ')))
mdict = {}
answer = ['-1'] * n
stack = []

for s in mlist:
    mdict[s] = mdict.get(s, 0) + 1

for i in range(n):
    while stack and mdict[mlist[i]] > mdict[mlist[stack[-1]]]:
        answer[stack.pop()] = str(mlist[i])
    stack.append(i)

print(' '.join(answer))