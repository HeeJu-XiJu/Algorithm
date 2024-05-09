import sys
sys.stdin = open('input.txt')

N = int(input())

dp = [[0, 0]]

dp.append([0, 1])
dp.append([0, 1])
dp.append([1, 1])

for i in range(4, N+1):
    dp.append([dp[i-1][0]+dp[i-1][1], dp[i-1][0]])

print(sum(dp[N]))