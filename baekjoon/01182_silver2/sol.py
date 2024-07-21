import sys
sys.stdin = open('input.txt')

N, S = map(int, input().split())
mlist= list(map(int, input().split()))

count = 0
answerlist = []

def dfs(s):
    global count
    if len(answerlist) > 0 and sum(answerlist) == S:
        count += 1
    for i in range(s, N):
        answerlist.append(mlist[i])
        dfs(i+1)
        answerlist.pop()
            
dfs(0)
print(count)