import sys
import math
sys.stdin = open('input.txt')

N, S = map(int, input().split())
bro = list(map(int, input().split()))
diff = []

for i in bro:
    diff.append(abs(i - S))

answer = min(diff)
for i in diff:
    answer = math.gcd(i, answer)

print(answer)