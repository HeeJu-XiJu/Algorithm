import sys
sys.stdin = open('input.txt')

n = int(input(), 8)

print(bin(n)[2:])