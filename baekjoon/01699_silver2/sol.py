import sys
sys.stdin = open('input.txt')

N = int(input())
dp = list(range(N+1))

for i in range(1, N+1):
    for j in range(1, int(i**(1/2))+1):
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1
print(dp[N])