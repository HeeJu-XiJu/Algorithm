import sys
sys.stdin = open('input.txt')

a, b = list(map(int,input().split()))
c = list(map(int,input().split()))

for number in range(a):
    if c[number] < b:
        print(c[number], end = " ")