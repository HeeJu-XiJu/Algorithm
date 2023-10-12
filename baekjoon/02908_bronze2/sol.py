import sys
sys.stdin = open('input.txt')

a, b = input().split()
sangsu_a = a[::-1]
sangsu_b = b[::-1]

if sangsu_a > sangsu_b:
    print(sangsu_a)
else:
    print(sangsu_b)