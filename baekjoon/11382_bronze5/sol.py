import sys
sys.stdin = open('input.txt')

A, B, C = list(map(int,input().split()))
print(A + B + C)