import sys
sys.stdin = open('input.txt')

n = int(input())
mlist = list(map(int, input().split(' ')))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if mlist[i] > mlist[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))