import sys

sys.stdin = open('input.txt')

a, b = map(int, input().split())

def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two_count(a) - two_count(a - b) - two_count(b), five_count(a) - five_count(a - b) - five_count(b)))