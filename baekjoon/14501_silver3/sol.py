import sys
sys.stdin = open('input.txt')

N = int(input())
daylist = []

for _ in range(N):
    day = list(map(int, input().split(' ')))
    daylist.append(day)

maxday = 0
count = 0

def dfs(s, count):
    global maxday
    if s >= N:
        maxday = max(maxday, count)
        return
    for i in range(s, N):
        A, B = daylist[i]
        if i+A <= N:
            dfs(i+A, count+B)
        else:
            dfs(i+A, count)

dfs(0, 0)
print(maxday)