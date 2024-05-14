import sys
sys.stdin = open('input.txt')

N = int(input())
mlist = list(map(int, input().split(' ')))

dp = [0] * N
dp[0] = mlist[0]

for i in range(1, N):
    dp[i] = max(mlist[i], dp[i-1] + mlist[i])

print(max(dp))