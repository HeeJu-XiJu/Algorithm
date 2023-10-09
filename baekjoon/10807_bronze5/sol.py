import sys
sys.stdin = open('input.txt')

T = int(input())
a = list(map(int,input().split()))
N = int(input())
result = 0

for number in range(T):
    if a[number] == N:
        result += 1
print(result)