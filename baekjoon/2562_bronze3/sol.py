import sys
sys.stdin = open('input.txt')

max = 0

for number in range(1, 10):
    N = int(input())
    if N > max :
        max = N
        value = number


print(max)
print(value)
