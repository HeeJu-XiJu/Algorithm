import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().rstrip())

for number in range(1, T+1):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    print(a + b)