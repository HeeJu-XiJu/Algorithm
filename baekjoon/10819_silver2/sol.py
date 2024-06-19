import sys
sys.stdin = open('input.txt')

N = int(input())
mlist = list(map(int, input().split(' ')))

visited = [False] * N
max_num = 0
arr = []
def dfs(s):
    global max_num
    if s == N:
        ans = 0
        for i in range(N-1):
            ans += abs(mlist[arr[i]] - mlist[arr[i+1]])
        max_num = max(max_num, ans)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(s+1)
            visited[i] = False
            arr.pop()

dfs(0)
print(max_num)