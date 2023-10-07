import sys
sys.stdin = open('input.txt')

T = int(input())

for numbers in range(1, T+1):
    a, b = list(map(int,input().split()))
    print(a + b)