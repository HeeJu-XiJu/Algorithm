import sys
sys.stdin = open('input.txt')

N = int(input())
member = []

for _ in range(N):
    member.append(list(map(int, input().split(' '))))

mincount = 200000000000
visited = [False] * N

def dfs(couple, idx):
    global mincount
    if couple == (N/2):
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] == True and visited[j] == True:
                    A += member[i][j]
                elif visited[i] == False and visited[j] == False:
                    B += member[i][j]
        mincount = min(mincount, abs(A-B))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(couple+1, i+1)
            visited[i] = False

dfs(0, 0)
print(mincount)