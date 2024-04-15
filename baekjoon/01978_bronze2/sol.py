import sys
sys.stdin = open('input.txt')

mlist = list(range(2, 1001))

for i in range(2, int(1001 ** (1/2)) + 1):
    for j in range(i+i, 1001, i):
        if j in mlist:
            mlist.remove(j)

n = int(input())
result = list(map(int, input().split()))
answer = 0

for i in result:
    if i in mlist:
        answer += 1

print(answer)