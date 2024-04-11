import sys
sys.stdin = open('input.txt')

mlist = list(input().split())

a = int(mlist[0] + mlist[1])
b = int(mlist[2] + mlist[3])

answer = a + b

print(answer)