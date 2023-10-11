import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(1, T + 1):
    a = input()
    result = a[0] + a[-1] 
    print(result)