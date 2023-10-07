import sys
sys.stdin = open('input.txt')

n = int(input())

print('long ' * (n // 4) + 'int')