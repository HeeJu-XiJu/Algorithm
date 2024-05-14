import sys
sys.stdin = open('input.txt')

N = int(input())
mlist = list(map(int, input().split(' ')))

dp = [0] * N

for i in range(N):
    for j in range(i):
        if dp[i] < dp[j] and mlist[i] > mlist[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))

answer = []
M = max(dp)

for i in range(N-1, -1, -1):
    if dp[i] == M:
        answer.append(mlist[i])
        M -= 1
    if M == 0:
        break

answer.reverse()
print(*answer)