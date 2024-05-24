import sys
sys.stdin = open('input.txt')

N = int(input())
M = int(input())

if M != 0:
    buttonlist = list(map(int, input().split(' ')))
else:
    buttonlist = []


mincount = abs(N-100)


for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in buttonlist:
            break
        elif j == len(num) - 1:
            mincount = min(mincount, len(num) + abs(int(num) - N))

print(mincount)