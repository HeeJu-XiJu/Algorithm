import sys
sys.stdin = open('input.txt')

def dfs(visited, idx):
    if visited == 6:
        print(' '.join(map(str, answer)))
        return
    for i in range(idx, k):
            answer.append(S[i])
            dfs(visited + 1, i + 1)
            answer.pop()

while True:
    S = list(map(int, input().split(' ')))
    k = S[0]
    S = S[1:]
    
    answer = []

    dfs(0, 0)

    if k == 0:
         exit()
    print()