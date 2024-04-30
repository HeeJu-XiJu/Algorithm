import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
n = int(input())
mlist = list(map(int, input().split()))
mlist.reverse()
num_10 = 0

for i in range(n):
    num_10 += A ** i * mlist[i]

answerlist = []
while num_10 >= 1:
    a = num_10 % B
    num_10 = num_10 // B

    answerlist.append(a)

print(' '.join(map(str, answerlist[::-1])))