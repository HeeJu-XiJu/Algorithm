import sys
sys.stdin = open('input.txt')

N = int(input())

for number in range(1, N+1):
    print((' ' * (N - number)) + ('*' * number))