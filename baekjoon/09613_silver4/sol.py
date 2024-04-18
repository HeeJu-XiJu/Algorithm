import sys
import math
sys.stdin = open('input.txt')

n = int(input())

for _ in range(n):
    mlist = list(map(int, input().split()))
    m = mlist[0]
    answer = 0
    for i in range(1, m+1):
        for j in range(i+1, m+1):
            answer += math.gcd(mlist[i], mlist[j])
    
    print(answer)