import sys
sys.stdin = open('input.txt')

numlist = [False, False] + [True]*(999999)

for i in range(2, 1000001):
    if numlist[i]:
        for j in range(i+i, 1000001, i):
            numlist[j] = False

n = int(input())
for _ in range(n):
    num = int(input())
    count = 0
    
    for i in range(2, num//2+1):
        if numlist[i] and numlist[num-i]:
            count += 1

    print(count)