import sys
from math import gcd
sys.stdin = open('input.txt')

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))