import sys
input = sys.stdin.readline

T = int(input())
print(T)

for number in range(1, T+1):
    a, b = list(map(int,input().split()))
    result = a + b
    print(result)