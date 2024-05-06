import sys
sys.stdin = open('input.txt')

N = int(input())
Plist = [0] + list(map(int, input().split(' ')))
dp = Plist

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[j] + Plist[i-j])

print(dp[N])